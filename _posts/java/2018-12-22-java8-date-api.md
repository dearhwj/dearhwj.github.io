---
layout: post
title: JAVA8新特性-日期对象和API
category: JAVA
keywords: 
---

## 新日期对象和API的特性
Java 8日期/时间API是JSR-310规范的实现，它的目标是克服旧的日期/时间API实现中所有的缺陷，新的日期/时间API的一些设计原则如下：

1. 不变性：新的日期/时间API中，所有的类都是不可变的，这种设计有利于并发编程。
2. 关注点分离：新的API将人可读的日期时间和机器时间（unix timestamp）明确分离，它为日期（Date）、时间（Time）、日期时间（DateTime）、时间戳（unix timestamp）以及时区定义了不同的类。
3. 清晰：在所有的类中，方法都被明确定义用以完成相同的行为。举个例子，要拿到当前实例我们可以使用now()方法，在所有的类中都定义了format()和parse()方法，而不是像以前那样专门有一个独立的类。为了更好的处理问题，所有的类都使用了工厂模式和策略模式，一旦你使用了其中某个类的方法，与其他类协同工作并不困难。
4.  实用操作：所有新的日期/时间API类都实现了一系列方法用以完成通用的任务，如：加、减、格式化、解析、从日期/时间中提取单独部分等操作。
5. 可扩展性：新的日期/时间API是工作在ISO-8601日历系统上的，但我们也可以将其应用在非IOS的日历上。


## LocalDate
Date对象表示特定的日期和时间，而LocalDate(Java8)对象只包含没有任何时间信息的日期。LocalDate是一个不可变的类，它表示默认格式(yyyy-MM-dd)的日期，我们可以使用now()方法得到当前时间，也可以提供输入年份、月份和日期的输入参数来创建一个LocalDate实例。该类为now()方法提供了重载方法，我们可以传入ZoneId来获得指定时区的日期。


## LocalTime
LocalTime是一个不可变的类，它的实例代表一个符合人类可读格式的时间，默认格式是hh:mm:ss.zzz。像LocalDate一样，该类也提供了时区支持，同时也可以传入小时、分钟和秒等输入参数创建实例。

## LocalDateTime
LocalDateTime是一个不可变的日期-时间对象，它表示一组日期-时间，默认格式是yyyy-MM-dd-HH-mm-ss.zzz。它提供了一个工厂方法，通过接收LocalDate和LocalTime输入参数，来创建LocalDateTime实例。


## Instant
Instant类是用在机器可读的时间格式上的，它以Unix时间戳的形式存储日期时间，我们来看一个简单的程序。


## ZonedDateTime
ZonedDateTime这是一个包含时区的完整的日期时间，偏移量是以UTC/格林威治时间为基准的。

## MonthDay
这个类由月日组合，不包含年信息，可以用来代表每年重复出现的一些日期或其他组合。他和新的日期库中的其他类一样也都是不可变且线程安全的，并且它还是一个值类（value class）。

## Period
计算两个日期之间包含多少天、周、月、年。可以用java.time.Period类完成该功能。

## ZoneOffset
在java8中，可以使用ZoneOffset来代表某个时区，可以使用它的静态方法ZoneOffset.of()方法来获取对应的时区，只要获得了这个偏移量，就可以用这个偏移量和LocalDateTime创建一个新的OffsetDateTime.可以看到现在时间日期和时区关联上了，注意OffsetDateTime主要是用来给机器理解的，平时使用就用前面结束的ZoneDateTime类就可以了

## DateTimeFormatter 
DateTimeFormatter类用于在Java中进行日期的格式化与解析。与SimpleDateFormat不同，它是不可变且线程安全的，如果需要的话，可以赋值给一个静态变量。DateTimeFormatter类提供了许多预定义的格式器，你也可以自定义自己想要的格式。当然了，根据约定，它还有一个parse()方法是用于将字符串转换成日期的，如果转换期间出现任何错误，它会抛出DateTimeParseException异常。类似的，DateFormatter类也有一个用于格式化日期的format()方法，它出错的话则会抛出DateTimeException异常。






### 参考资料
* [https://www.cnblogs.com/chenpi/p/5970172.html](https://www.cnblogs.com/chenpi/p/5970172.html)
* [https://www.cnblogs.com/comeboo/p/5378922.html](https://www.cnblogs.com/comeboo/p/5378922.html)

