---
layout: post
title: JAVA线程池设定
category: JAVA
keywords: 
---

## Future 接口的局限性

`Future`接口可以构建异步应用，但依然有其局限性。它很难直接表述多个Future 结果之间的依赖性。实际开发中，我们经常需要达成以下目的：

* 将两个异步计算合并为一个——这两个异步计算之间相互独立，同时第二个又依赖于第一个的结果。
* 等待 Future 集合中的所有任务都完成。
* 仅等待 Future集合中最快结束的任务完成（有可能因为它们试图通过不同的方式计算同一个值），并返回它的结果。
* 通过编程方式完成一个Future任务的执行（即以手工设定异步操作结果的方式）。
* 应对 Future 的完成事件（即当 Future 的完成事件发生时会收到通知，并能使用 Future 计算的结果进行下一步的操作，不只是简单地阻塞等待操作的结果）

新的CompletableFuture类将使得这些成为可能。

## CompletableFuture

JDK1.8才新加入的一个实现类`CompletableFuture`，实现了`Future<T>`, `CompletionStage<T>`两个接口。

当一个Future可能需要显示地完成时，使用`CompletionStage`接口去支持完成时触发的函数和操作。

当两个及以上线程同时尝试完成、异常完成、取消一个`CompletableFuture`时，只有一个能成功。

`CompletableFuture`实现了`CompletionStage`接口的如下策略：

1.  为了完成当前的`CompletableFuture`接口或者其他完成方法的回调函数的线程，提供了非异步的完成操作。

2.  没有显式入参`Executor`的所有`async`方法都使用`ForkJoinPool.commonPool()`为了简化监视、调试和跟踪，所有生成的异步任务都是标记接口`AsynchronousCompletionTask`的实例。

3.  所有的`CompletionStage`方法都是独立于其他共有方法实现的，因此一个方法的行为不会受到子类中其他方法的覆盖。

`CompletableFuture`实现了`Futurre`接口的如下策略：

1.  `CompletableFuture`无法直接控制完成，所以`cancel`操作被视为是另一种异常完成形式。方法`isCompletedExceptionally`可以用来确定一个`CompletableFuture`是否以任何异常的方式完成。

2.  以一个`CompletionException`为例，方法`get()`和`get(long,TimeUnit)`抛出一个`ExecutionException`，对应`CompletionException`。为了在大多数上下文中简化用法，这个类还定义了方法`join()`和`getNow`，而不是直接在这些情况中直接抛出`CompletionException`。

`CompletableFuture`中4个异步执行任务静态方法：

```hljs
public static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier) {
        return asyncSupplyStage(asyncPool, supplier);
    }

public static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier,Executor executor) {
    return asyncSupplyStage(screenExecutor(executor), supplier);
}

public static CompletableFuture<Void> runAsync(Runnable runnable) {
    return asyncRunStage(asyncPool, runnable);
}

public static CompletableFuture<Void> runAsync(Runnable runnable, Executor executor) {
    return asyncRunStage(screenExecutor(executor), runnable);
}
```



其中`supplyAsync`用于有返回值的任务，`runAsync`则用于没有返回值的任务。`Executor`参数可以手动指定线程池，否则默认`ForkJoinPool.commonPool()`系统级公共线程池，   
注意：**这些线程都是Daemon线程，主线程结束Daemon线程不结束，只有JVM关闭时，生命周期终止**。

## 异常处理

CompletableFuture实现了Future接口，因此你可以像Future那样使用它。

其次，CompletableFuture并非一定要交给线程池执行才能实现异步，你可以像下面这样实现异步运行：

```hljs
@Test
public void test1() throws ExecutionException, InterruptedException {
    CompletableFuture<String> completableFuture = new CompletableFuture<>();
    new Thread(() -> {
        // 模拟执行耗时任务
        System.out.println("task doing...");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 告诉completableFuture任务已经完成
        completableFuture.complete("ok");
    }).start();
    // 获取任务结果，如果没有完成会一直阻塞等待
    String result = completableFuture.get();
    System.out.println("计算结果:" + result);
}
```



如果没有意外，上面发的代码工作得很正常。但是，如果任务执行过程中产生了异常会怎样呢？

非常不幸，这种情况下你会得到一个相当糟糕的结果：异常会被限制在执行任务的线程的范围内，最终会杀死该线程，而这会导致等待`get`方法返回结果的线程永久地被阻塞。

客户端可以使用重载版本的`get` 方法，它使用一个超时参数来避免发生这样的情况。这是一种值得推荐的做法，你应该尽量在你的代码中添加超时判断的逻辑，避免发生类似的问题。

使用这种方法至少能防止程序永久地等待下去，超时发生时，程序会得到通知发生了`TimeoutException` 。不过，也因为如此，你不能确定执行任务的线程内到底发生了什么问题。

为了能获取任务线程内发生的异常，你需要使用   
CompletableFuture的`completeExceptionally`方法将导致CompletableFuture内发生问题的异常抛出。这样，当执行任务发生异常时，调用`get()`方法的线程将会收到一个 `ExecutionException`异常，该异常接收了一个包含失败原因的Exception 参数。

```hljs
@Test
public void test2() throws ExecutionException, InterruptedException {
    CompletableFuture<String> completableFuture = new CompletableFuture<>();
    new Thread(() -> {
        // 模拟执行耗时任务
        System.out.println("task doing...");
        try {
            Thread.sleep(3000);
            int i = 1/0;
        } catch (Exception e) {
            // 告诉completableFuture任务发生异常了
            completableFuture.completeExceptionally(e);
        }
        // 告诉completableFuture任务已经完成
        completableFuture.complete("ok");
    }).start();
    // 获取任务结果，如果没有完成会一直阻塞等待
    String result = completableFuture.get();
    System.out.println("计算结果:" + result);
}
```


## 举个栗子

JDK CompletableFuture  自带多任务组合方法allOf和anyOf

`allOf`是等待所有任务完成，构造后CompletableFuture完成

`anyOf`是只要有一个任务完成，构造后CompletableFuture就完成

其它方法的中文解释查看此文☞ https://www.jianshu.com/p/6f3ee90ab7d3

```
public class CompletableFutureDemo {
    public static void main(String[] args) {
        Long start = System.currentTimeMillis();
        // 结果集
        List<String> list = new ArrayList<>();

        ExecutorService executorService = Executors.newFixedThreadPool(10);

        List<Integer> taskList = Arrays.asList(2, 1, 3, 4, 5, 6, 7, 8, 9, 10);
        // 全流式处理转换成CompletableFuture[]+组装成一个无返回值CompletableFuture，join等待执行完毕。返回结果whenComplete获取
        CompletableFuture[] cfs = taskList.stream()
                .map(integer -> CompletableFuture.supplyAsync(() -> calc(integer), executorService)
                                .thenApply(h->Integer.toString(h))
                                .whenComplete((s, e) -> {
                                    System.out.println("任务"+s+"完成!result="+s+"，异常 e="+e+","+new Date());
                                    list.add(s);
                                })
                ).toArray(CompletableFuture[]::new);
        // 封装后无返回值，必须自己whenComplete()获取
        CompletableFuture.allOf(cfs).join();
        System.out.println("list="+list+",耗时="+(System.currentTimeMillis()-start));
    }

    public static Integer calc(Integer i) {
        try {
            if (i == 1) {
                Thread.sleep(3000);//任务1耗时3秒
            } else if (i == 5) {
                Thread.sleep(5000);//任务5耗时5秒
            } else {
                Thread.sleep(1000);//其它任务耗时1秒
            }
            System.out.println("task线程：" + Thread.currentThread().getName()
                    + "任务i=" + i + ",完成！+" + new Date());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return i;
    }
}
```



## 常用多线程并发，取结果归集的几种实现方案

描述        | Future                | FutureTask                                                | CompletionService                            | CompletableFuture                 
--------- | --------------------- | --------------------------------------------------------- | -------------------------------------------- | ----------------------------------
原理        | Future接口              | 接口RunnableFuture的唯一实现类，RunnableFuture接口继承自Future+Runnable | 内部通过阻塞队列+FutureTask接口                        | JDK8实现了Future, CompletionStage两个接口
多任务并发执行   | 支持                    | 支持                                                        | 支持                                           | 支持                                
获取任务结果的顺序 | 按照提交顺序获取结果            | 未知                                                        | 支持任务完成的先后顺序                                  | 支持任务完成的先后顺序                       
异常捕捉      | 自己捕捉                  | 自己捕捉                                                      | 自己捕捉                                         | 原生API支持，返回每个任务的异常                 
建议        | CPU高速轮询，耗资源，可以使用，但不推荐 | 功能不对口，并发任务这一块多套一层，不推荐使用                                   | **推荐使用，没有JDK8CompletableFuture之前最好的方案，没有质疑** | **API极端丰富，配合流式编程，速度飞起，推荐使用！**     

上表来源：https://www.cnblogs.com/dennyzhangdd/p/7010972.html

参考：

https://www.jianshu.com/p/4897ccdcb278

https://www.cnblogs.com/dennyzhangdd/p/7010972.html