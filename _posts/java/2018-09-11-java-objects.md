---
layout: post
title:  java.util.Objects 简介
category: JAVA
keywords: java.util.Objects mbda
---
## java.util.Object的方法
参考资料 [java.util.Objects 源码学习](https://blog.csdn.net/lkforce/article/details/56289349)

```
public static <T> int compare(T a, T b, Comparator<? super T> c)
```

比较对象a和对象b，如果a和b是相等的，返回0，如果不相等，调用c的compare方法。
注意：如果a或者b是null的情况下，调用c的compare方法时有可能报空指针异常，看c的compare方法怎么写了。

```
public static boolean equals(Object a, Object b)
```

比较对象a和对象b，使用的是第一个参数的equals()方法，
如果两个参数中有一个是null，则返回false，
如果两个参数都是null，则返回true。

```
public static boolean deepEquals(Object a, Object b)
```

比较对象a和对象b是否深度相等，使用的其实是Arrays.deepEquals()方法
只有a和b对应位置的元素都相等时，才返回true，a好b都是null也返回true，否则返回false。

```
public static int hash(Object... values)
```

得到一列对象的hash code，
使用的其实是Arrays.hashCode(Object[])，Object[]数组元素就是hash方法传入的参数值

```
public static int hashCode(Object o)
```
得到一个对象的hash code，如果参数为null，返回0

```
public static <T> T requireNonNull(T obj)
```
判断一个对象是不是null，如果不是null则返回对象本身，如果是null则抛出空指针异常。

```
public static <T> T requireNonNull(T obj,String message)
```
判断一个对象是不是null，如果不是null则返回对象本身，如果是null则抛出空指针异常，并把第二个参数message写在异常信息中

```
public static String toString(Object o)
```
调用对象的toString()方法，如果参数是null，返回字符串"null"

```
public static String toString(Object o, String nullDefault)
```
调用对象的toString()方法，如果参数是null，返回第二个参数表示的字符串
