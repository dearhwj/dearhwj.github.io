---
layout: post
title: Java线程池类ThreadPoolExecutor、ScheduledThreadPoolExecutor及Executors工厂类
category: JAVA
keywords: Java线程池
---
## 正文

原文地址:[https://blog.csdn.net/suifeng3051/article/details/49444177](https://blog.csdn.net/suifeng3051/article/details/49444177)

Java中的线程池类有两个，分别是：ThreadPoolExecutor和ScheduledThreadPoolExecutor，这两个类都继承自[ExecutorService](http://blog.csdn.net/suifeng3051/article/details/49443835)。利用这两个类，可以创建各种不同的Java线程池，为了方便我们创建线程池，Java API提供了Executors工厂类来帮助我们创建[各种各样](https://www.baidu.com/s?wd=%E5%90%84%E7%A7%8D%E5%90%84%E6%A0%B7&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)的线程池。下面我们分别介绍一下这三个类。

Java线程池ExecutorService继承树：

![这里写图片描述](https://img-blog.csdn.net/20151027094316987)

### 一、ThreadPoolExecutor

**ThreadPoolExecutor**是ExecutorService的一个实现类，也是java中最常用的线程池类。ThreadPoolExecutor内部维持了一个线程池，可以执行给定的任务，下面是关于它的具体使用方法。

### 1.1 ThreadPoolExecutor构造方法及其作用

ThreadPoolExecutor源码中的构造方法：

![这里写图片描述](https://img-blog.csdn.net/20151027094440811)


```
- corePoolSize：线程池维护线程的最少数量
- maximumPoolSize：线程池维护线程的最大数量
- keepAliveTime： 线程池维护线程所允许的空闲时间
- unit： 线程池维护线程所允许的空闲时间的单位
- workQueue： 线程池所使用的缓冲队列
- handler： 线程池对拒绝任务的处理策略
```


### 1.2 线程数量控制

ThreadPoolExecutor线程池中的线程数量是可变的，其变化范围取决于下面两个变量：


```
1. corePoolSize：线程池维护线程的最少数量
2. maximumPoolSize：线程池维护线程的最大数量
```

具体线程的分配方式是，当一个任务被添加到线程池：


```
1. 如果此时线程池中的数量小于corePoolSize，即使线程池中的线程都处于空闲状态，也要创建新的线程来处理被添加的任务。
2. 如果此时线程池中的数量等于 corePoolSize，但是缓冲队列 workQueue未满，那么任务被放入缓冲队列。
3. 如果此时线程池中的数量大于corePoolSize，缓冲队列workQueue满，并且线程池中的数量小于maximumPoolSize，建新的线程来处理被添加的任务。
4. 如果此时线程池中的数量大于corePoolSize，缓冲队列workQueue满，并且线程池中的数量等于maximumPoolSize，那么通过 handler所指定的策略来处理此任务。也就是：处理任务的优先级为：核心线程corePoolSize、任务队列workQueue、最大线程maximumPoolSize，如果三者都满了，使用handler处理被拒绝的任务。
5. 当线程池中的线程数量大于 corePoolSize时，如果某线程空闲时间超过keepAliveTime，线程将被终止。
```


这样，线程池可以动态的调整池中的线程数。除了`corePoolSize`、`maximumPoolSize`两个变量外，ThreadPoolExecutor构造方法还有几个参数：


```has-numbering
- keepAliveTime： 线程池维护线程所允许的空闲时间
- unit： 线程池维护线程所允许的空闲时间的单位
- workQueue： 线程池所使用的缓冲队列
- handler： 线程池对拒绝任务的处理策略
```


### 1.2 unit

unit 可选的参数为`java.util.concurrent.TimeUnit`中的几个静态属性：


```
- NANOSECONDS
- MICROSECONDS
- MILLISECONDS
- SECONDS
```



### 1.3 workQueue

workQueue是一个[BlockingQueue](http://blog.csdn.net/suifeng3051/article/details/48807423)，默认是`LinkedBlockingQueue<Runnable>`

### 1.4 handler

handler 是线程池拒绝处理任务的方式，主要有四种类型：

1.  ThreadPoolExecutor.AbortPolicy()（系统默认）：抛出java.util.concurrent.RejectedExecutionException异常
2.  ThreadPoolExecutor.CallerRunsPolicy()：当抛出RejectedExecutionException异常时，会调用rejectedExecution方法
3.  ThreadPoolExecutor.DiscardOldestPolicy()：抛弃旧的任务
4.  ThreadPoolExecutor.DiscardPolicy()：抛弃当前的任务

### 1.5 创建一个ThreadPoolExecutor

```
int  corePoolSize  =    5;
int  maxPoolSize   =   10;
long keepAliveTime = 5000;

ExecutorService threadPoolExecutor =
    new ThreadPoolExecutor(
            corePoolSize,
            maxPoolSize,
            keepAliveTime,
            TimeUnit.MILLISECONDS,
                new LinkedBlockingQueue<Runnable>()
            );
```

  

### 二、ScheduledThreadPoolExecutor

    **ScheduledThreadPoolExecutor**是ExecutorService的另一个实现类，从上面Java线程池ExecutorService继承树这幅图可以看出，ScheduledThreadPoolExecutor直接继承自**ScheduledExecutorService**，ScheduledThreadPoolExecutor 类的功能也主要体现在ScheduledExecutorService 接口上，而所以在介绍ScheduledThreadPoolExecutor之前先介绍一下ScheduledExecutorService接口。

    ### 2.1 ScheduledExecutorService接口介绍

    `java.util.concurrent.ScheduledExecutorService`接口继承了ExecutorService，它的最主要的功能就是可以对其中的任务进行调度，比如延迟执行、定时执行等等。

    ScheduledExecutorService接口定义：


    ```has-numbering
    public interface ScheduledExecutorService extends ExecutorService {

        public ScheduledFuture<?> schedule(Runnable command, long delay, TimeUnit unit);


        public ScheduledFuture<?> scheduleAtFixedRate(Runnable command,long initialDelay, long period, TimeUnit unit);

        public ScheduledFuture<?> scheduleWithFixedDelay(Runnable command,long initialDelay, long delay,TimeUnit unit);

    }
    ```

    * 1
    * 2
    * 3
    * 4
    * 5
    * 6
    * 7
    * 8
    * 9
    * 10


    从上面接口定义我们知道，提供了四个方法，下面我们就分别介绍：


    ```has-numbering
    1. schedule (Runnable task, long delay, TimeUnit timeunit)
    2. schedule (Callable task, long delay, TimeUnit timeunit)
    3. scheduleAtFixedRate (Runnable, long initialDelay, long period, TimeUnit timeunit)
    4. scheduleWithFixedDelay (Runnable, long initialDelay, long period, TimeUnit timeunit)
    ```

    * 1
    * 2
    * 3
    * 4


    #### 2.1.1  schedule (Runnable task, long delay, TimeUnit timeunit)

    这个方法的意思是在指定延迟之后运行task。这个方法有个问题，就是没有办法获知task的执行结果。如果我们想获得task的执行结果，我们可以传入一个Callable的实例（后面会介绍）。


    ```has-numbering
    ScheduledExecutorService scheduledExecutorService =
        Executors.newScheduledThreadPool(5);

    ScheduledFuture scheduledFuture =
    scheduledExecutorService.schedule(new Callable() {
        public Object call() throws Exception {
            System.out.println("Executed!");
            return "Called!";
        }
    },
    5,
    TimeUnit.SECONDS);
    System.out.println("result = " + scheduledFuture.get());
    scheduledExecutorService.shutdown();
    ```

    * 1
    * 2
    * 3
    * 4
    * 5
    * 6
    * 7
    * 8
    * 9
    * 10
    * 11
    * 12
    * 13
    * 14


    #### 2.1.2 schedule (Callable task, long delay, TimeUnit timeunit)

    这个方法与`schedule (Runnable task)`类似，也是在指定延迟之后运行task，不过它接收的是一个Callable实例，此方法会返回一个ScheduleFuture对象，通过ScheduleFuture我们可以取消一个未执行的task，也可以获得这个task的执行结果。


    ```has-numbering
    ScheduledExecutorService scheduledExecutorService =
        Executors.newScheduledThreadPool(5);

    ScheduledFuture scheduledFuture =
    scheduledExecutorService.schedule(new Callable() {
        public Object call() throws Exception {
            System.out.println("Executed!");
            return "Called!";
        }
    },
    5,
    TimeUnit.SECONDS);

    System.out.println("result = " + scheduledFuture.get());
    scheduledExecutorService.shutdown();
    ```

    * 1
    * 2
    * 3
    * 4
    * 5
    * 6
    * 7
    * 8
    * 9
    * 10
    * 11
    * 12
    * 13
    * 14
    * 15


    #### 2.1.3 scheduleAtFixedRate (Runnable, long initialDelay, long period, TimeUnit timeunit)

    这个方法的作用是周期性的调度task执行。task第一次执行的延迟根据`initialDelay`参数确定，以后每一次执行都间隔`period`时长。

    如果task的执行时间大于定义的period，那么下一个线程将在当前线程完成之后再执行。整个调度保证不会出现一个以上任务同时执行。

    #### 2.1.4 scheduleWithFixedDelay (Runnable, long initialDelay, long period, TimeUnit timeunit)

    scheduleWithFixedDelay的参数和scheduleAtFixedRate参数完全一致，它们的不同之处在于对period调度周期的解释。

    在scheduleAtFixedRate中，period指的两个任务开始执行的时间间隔，也就是当前任务的开始执行时间和下个任务的开始执行时间之间的间隔。

    而在scheduleWithFixedDelay中，period指的当前任务的**结束**执行时间到下个任务的开始执行时间。

    #### 2.1.5 ScheduledExecutorService的关闭

    和ExecutorService类似, 我们在使用完ScheduledExecutorService时需要关闭它。如果不关闭的话，JVM会一直运行直，即使所有线程已经关闭了。

    关闭ScheduledExecutorService可以使用其继承自ExecutorService接口的`shutdown()`和`shutdownNow()`方法，两者的区别请参考【[Java线程池 ExecutorService](http://blog.csdn.net/suifeng3051/article/details/49443835)】。

    ### 2.2 ScheduledThreadPoolExecutor

    ScheduledThreadPoolExecutor继承自ThreadPoolExecutor，构造参数很简单，只有3个：


    ```has-numbering
    1. int corePoolSize：线程池维护线程的最少数量
    2. ThreadFactory threadFactory：线程工程类，线程池用它来制造线程
    3. RejectedExecutionHandler handler：线程池对拒绝任务的处理策略
    ```

    * 1
    * 2
    * 3


    具体使用方法请参考ThreadPoolExecutor或者使用Executors。

    ## 三、Executors

    创建一个什么样的ExecutorService的实例（即线程池）需要我们的具体应用场景而定，不过Java给我们提供了一个Executors工厂类，它可以帮助我们很方便的创建各种类型ExecutorService线程池，Executors一共可以创建下面这四类线程池：


    ```has-numbering
    1. newCachedThreadPool 创建一个可缓存线程池，如果线程池长度超过处理需要，可灵活回收空闲线程，若无可回收，则新建线程。
    2. newFixedThreadPool 创建一个定长线程池，可控制线程最大并发数，超出的线程会在队列中等待。
    3. newScheduledThreadPool 创建一个定长线程池，支持定时及周期性任务执行。
    4. newSingleThreadExecutor 创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，保证所有任务按照指定顺序(FIFO, LIFO, 优先级)执行。
    ```

    * 1
    * 2
    * 3
    * 4


    备注：Executors只是一个工厂类，它所有的方法返回的都是ThreadPoolExecutor、ScheduledThreadPoolExecutor这两个类的实例。
