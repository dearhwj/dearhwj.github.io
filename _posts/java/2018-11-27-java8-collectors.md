---
layout: post
title: Java 8的新特性Collectors
category: JAVA
keywords: JAVA8
---

## 正文

### Collectors.joining()字符串连接

Collectors.joining() 方法用某个指定的拼接字符串把所有元素拼接成一个字符串，并添加可选的前缀和后缀

```

public class JoiningExample {
    public static void main(String[] args) {
       List<String> list = Arrays.asList("A","B","C","D");
       String result=  list.stream().collect(Collectors.joining(",","(",")"));
       System.out.println(result);
    }
}


```

### Collectors.maxBy() 和 Collectors.minBy()计算最大值和最小值


Collectors.maxBy() 和 Collectors.minBy() 两个方法分别用于计算流中所有元素的最大值和最小值。

两个方法都可以接受一个比较器作为参数，用于如何计算最大值或最小值

```
package cn.twle.util.stream;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
public class MaxByMinByExample {
    public static void main(String[] args) {
       List<Integer> list = Arrays.asList(30,10,20,35);
       //Get Max       
       list.stream().collect(Collectors.maxBy(new MaxByMinByExample().new IntegerComp()))
               .ifPresent(i->System.out.println(i));
       //Get Min
       list.stream().collect(Collectors.minBy(new MaxByMinByExample().new IntegerComp()))
               .ifPresent(i->System.out.println(i));
    }
    class IntegerComp implements Comparator<Integer> {
        @Override
        public int compare(Integer i1, Integer i2) {
          if(i1 >=i2 ){
              return 1;
          }else{
              return -1;
          }
        }
    }
}

```

### Collectors.summingInt()计算综合
Collectors.summingInt() 方法将流中的所有元素视为 int 类型，并计算所有元素的总和 ( sum )

```
package cn.twle.util.stream;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
public class SummingIntExample {
    public static void main(String[] args) {
       List<Integer> list = Arrays.asList(30,10,20,35);
       int result = list.stream().collect(Collectors.summingInt(i->i));
       System.out.println(result);
    }
}
```
输出结果为 

```
95
```

### Collectors.toList()导出到一个列表 ( List ) 

```

public class ToListExample {
    public static void main(String[] args) {
       List<String> list = Stream.of("AA","BB","CC").collect(Collectors.toList());
       list.forEach(s->System.out.println(s));
    }
}


```

### Collectors.toSet()
Collectors.toSet() 把流中的所有元素导出到一个集合 ( Set ) 中，并排除重复的元素 ( Set 的特性 )


```
public class ToSetExample {
    public static void main(String[] args) {
       Set<String> set = Stream.of("AA","AA","BB").collect(Collectors.toSet());
       set.forEach(s->System.out.println(s));
    }
}

```


    
### Collectors.toMap()

Collectors.toMap() 将流中的所有元素导出到一个哈希表 ( Map ) 中。该方法接受两个参数，第一个参数用于生成键 ( key ) ，第二个参数用于生成值 ( value )。两个参数都是 Lambda 表达式。

```
public class ToMapExample {
    public static void main(String[] args) {
       Map<String,String> map = Stream.of("AA","BB","CC").collect(Collectors.toMap(k->k, v->v+v));
       map.forEach((k,v)->System.out.println("key:"+k +"  value:"+v));
    }
    
    
```

### Collectors.mapping()

Collectors.mapping() 一般用于多重 map and reduce 中。 Java 文档中描述的原型如下

```
public class MappingDemo {
    public static void main(String[] args) {
        List<Person> list = Person.getList();
        Map<Integer, String> nameByAge
           = list.stream().collect(Collectors.groupingBy(Person::getAge, 
                   Collectors.mapping(Person::getName, Collectors.joining(","))));
        nameByAge.forEach((k,v)->System.out.println("Age:"+k +"  Persons: "+v));
    }   
}


```

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

### 分组排序再计算

三个参数的 groupingBy() 方法的原型如下

```
Collector<T,?,M> groupingBy(Function<? super T,? extends K> classifier, Supplier<M> mapFactory, Collector<? super T,A,D> downstream)

```

对于这个重载方法，我们可以简单的用六个字来归纳功能 分组预处理再计算，预处理可以是 排序

比如我们要对雇员按照部门分组，然后对部门进行排序，最后计算部门的平均薪水，可以如下实现

```
Map<String, Double> averageSalaryDeptSorted = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment, TreeMap::new, Collectors.averagingDouble(Employee::getSalary)));
System.out.println(averageSalaryDeptSorted);
```

因为使用了 TreeMap ，所以需要引入 java.util.TreeMap 类

运行结果如下

```
{Benefits=300.99, IT=250.99, Sales=250.49}
```


### 并行分组处理
多核时代，对于分组这种功能，没有充分利用多核功能是否有点太可惜了，Java 估计就是这么认为的，所以提供了并行分组方法 groupingByConcurrent()

groupingByConcurrent() 方法会返回一个 ConcurrentHashMap 类型的数据

该方法使用方式和 groupingBy 一样，我们就直接上范例吧

```
Map<String, Long> deptEmpCount3 = employees.stream().collect(Collectors.groupingByConcurrent(Employee::getDepartment, Collectors.counting())); 
System.out.println(deptEmpCount3)
```

运行结果如下

```
{Sales=2, IT=2, Benefits=1}
```




## 参考
* [Java 流收集器 ( Stream Collectors ) ( 三 ) - 分组元素 ( grouping )](https://www.twle.cn/t/139)
* [Java8 收集器 - java.util.stream.Collectors](https://www.twle.cn/c/yufei/java8/java8-basic-util-stream-collectors.html)


