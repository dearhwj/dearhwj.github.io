---
layout: post
title: Java 8的新特性Collectors
category: JAVA
keywords: JAVA8
---

## 正文
### Collectors.groupingBy() 分组

Collectors 提供了 groupingBy() 用于分组元素，该方法接受两个参数，就是分组器和分组之后要做的进一步处理，然后返回一个 Map<K,List<T>>> 的哈希表

```
Map<String, List<Employee>> deptEmps = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment));
System.out.println(deptEmps);
```

### Collectors.counting() 计数

从 groupingBy() 的原型中可以看出，该方法还接受第二个参数，就是分组后的进一步处理，我可以利用这个参数做一些其它的事情，比如计数 counting()

```
Map<String, Long> deptEmpsCount = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
System.out.println(deptEmpsCount);
```

## 参考


