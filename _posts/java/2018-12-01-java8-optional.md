---
layout: post
title: Java 8的新特性Optional
category: JAVA
keywords: JAVA8
---

## 正文
从 Java 8 引入的一个很有趣的特性是 Optional  类。Optional 类主要解决的问题是臭名昭著的空指针异常（NullPointerException） —— 每个 Java 程序员都非常了解的异常。
本质上，这是一个包含有可选值的包装类，这意味着 Optional 类既可以含有对象也可以为空。

Optional 是 Java 实现函数式编程的强劲一步，并且帮助在范式中实现。但是 Optional 的意义显然不止于此。


### 创建 Optional  实例
你可以使用  of() 和 ofNullable() 方法创建包含值的 Optional。两个方法的不同之处在于如果你把 null 值作为参数传递进去，of() 方法会抛出 NullPointerException


### 访问 Optional 对象的值
从 Optional 实例中取回实际值对象的方法之一是使用 get() 方法，这个方法会在值为 null 的时候抛出异常。要避免异常，你可以选择首先验证是否有值。检查是否有值的另一个选择是 ifPresent() 方法。该方法除了执行检查，还接受一个Consumer(消费者) 参数，如果对象不是空的，就对执行传入的 Lambda 表达式。

```
opt.ifPresent( u -> assertEquals(user.getEmail(), u.getEmail()));

```


### 返回默认值
* orElse()，它的工作方式非常直接，如果有值则返回该值，否则返回传递给它的参数值
* orElseGet() —— 其行为略有不同。这个方法会在有值的时候返回值，如果没有值，它会执行作为参数传入的 Supplier(供应者) 函数式接口，并将返回其执行结果


### 返回异常
除了 orElse() 和 orElseGet() 方法，Optional 还定义了 orElseThrow() API —— 它会在对象为空的时候抛出异常


### 转换值
有很多种方法可以转换 Optional的值。
* map() 对值应用(调用)作为参数的函数，然后将返回的值包装在 Optional 中
* flatMap() 也需要函数作为参数，并对值调用这个函数，然后直接返回结果



### 过滤值

除了转换值之外，Optional  类也提供了按条件“过滤”值的方法。

filter() 接受一个 Predicate 参数，返回测试结果为 true 的值。如果测试结果为 false，会返回一个空的 Optional。

```
@Test
public void whenFilter_thenOk() {
    User user = new User("anna@gmail.com", "1234");
    Optional<User> result = Optional.ofNullable(user)
      .filter(u -> u.getEmail() != null && u.getEmail().contains("@"));

    assertTrue(result.isPresent());
}

```


### 如何正确使用Optional
原文地址[https://blog.kaaass.net/archives/764](https://blog.kaaass.net/archives/764)


```
public static String getName(User u) {
    Optional<User> user = Optional.ofNullable(u);
    if (!user.isPresent())
        return "Unknown";
    return user.get().name;
}
```

这样改写非但不简洁，而且其操作还是和第一段代码一样。无非就是用isPresent方法来替代u==null。这样的改写并不是Optional正确的用法，我们再来改写一次。

```
public static String getName(User u) {
    return Optional.ofNullable(u)
                    .map(user->user.name)
                    .orElse("Unknown");
}
```

这样才是正确使用Optional的姿势。



### 在 Java 8 中提高 Null 的安全性
原文  [在 Java 8 中避免 Null 检查](http://www.importnew.com/28387.html)

通过利用 Java 8 的 Optional 类型来摆脱所有这些 null 检查。map 方法接收一个 Function 类型的 lambda 表达式，并自动将每个 function 的结果包装成一个 Optional 对象。这使我们能够在一行中进行多个 map 操作。Null 检查是在底层自动处理的。

```

Optional.of(new Outer())
    .map(Outer::getNested)
    .map(Nested::getInner)
    .map(Inner::getFoo)
    .ifPresent(System.out::println);
```

还有一种实现相同作用的方式就是通过利用一个 supplier 函数来解决嵌套路径的问题：

```
Outer obj = new Outer();
resolve(() -> obj.getNested().getInner().getFoo());
    .ifPresent(System.out::println);
```

调用 obj.getNested().getInner().getFoo()) 可能会抛出一个 NullPointerException 异常。在这种情况下，该异常将会被捕获，而该方法会返回 Optional.empty()。

```
public static <T> Optional<T> resolve(Supplier<T> resolver) {
    try {
        T result = resolver.get();
        return Optional.ofNullable(result);
    }
    catch (NullPointerException e) {
        return Optional.empty();
    }
}

```

