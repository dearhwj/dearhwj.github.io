---
layout: post
title: JAVA8 Supplier接口
category: JAVA
keywords: JAVA8
---


## 正文
原文地址[https://blog.csdn.net/qq_28410283/article/details/80625482](https://blog.csdn.net/qq_28410283/article/details/80625482)


看下接口定义

```
@FunctionalInterface
public interface Supplier<T> {
 
    /**
     * Gets a result.
     *
     * @return a result
     */
    T get();
}
```

supplier
英 [səˈplaɪə(r)]   美 [səˈplaɪər]  
n.
供应商;供应国;供应者，供给者;补充者

看语义，可以看到，这个接口是一个提供者的意思，只有一个get的抽象类，没有默认的方法以及静态的方法，传入一个泛型T的，get方法，返回一个泛型T
下面，我们用一个小案例，来看看这个接口，是干什么用的

```
Supplier<String> supplier = String::new;
        System.out.println(supplier.get());//""
        Supplier<Emp> supplierEmp = Emp::new;
        Emp emp = supplierEmp.get();
        emp.setName("dd");
        System.out.println(emp.getName());//dd
```


可以看到，这个接口，只是为我们提供了一个创建好的对象，这也符号接口的语义的定义，提供者，提供一个对象，
直接理解成一个创建对象的工厂，就可以了；

Emp对象定义如下

```
public static class Emp {
        private String name;
 
        public Emp() {
 
        }
 
        public Emp(String name) {
            super();
            this.name = name;
        }
 
        public String getName() {
            return name;
        }
 
        public void setName(String name) {
            this.name = name;
        }
 
    }
```