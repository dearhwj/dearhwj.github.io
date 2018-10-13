---
layout: post
title: JDK7的AutoCloseable接口
category: JAVA
keywords: AutoCloseable
---

## 正文
接口AutoCloseable是jdk1.7出现的新接口，存在于java.lang包中，可配合jdk1.7出现的try-with-resources新语法特性一起使用，用于自动关闭某个系统资源，如：文件，网络等。该接口只定义了一个方法：

```
class MyResource implements AutoCloseable{

    @Override
    public void close() {
        System.out.println("closed");
    }

    public void test() {
    }
}


public class AutoCloseableStudy {

    public static void main(String[] args) {
        try(MyResource resource = new MyResource()){
            resource.test();
        }
    }

}

```


防止业务代码的异常被Suppressed，如上代码，try代码块中可能会抛出异常，而finally代码块中也有可能抛出异常，当两个异常都同时抛出时，try代码块中所抛出的异常会被suppressed掉，所以往往捕获的异常不是我们想要的，而在try-with-resources代码块中的异常可以正常抛出，相反，close方法所抛出的异常会被suppressed掉。