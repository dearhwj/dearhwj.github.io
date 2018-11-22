---
layout: post
title: Java 8的新特性@FunctionalInterface
category: JAVA
keywords: JAVA8
---

## 正文

原文地址:[https://blog.csdn.net/qq_36372507/article/details/78757811](https://blog.csdn.net/qq_36372507/article/details/78757811)

在java8中，满足下面任意一个条件的接口都是函数式接口：

1、被@FunctionalInterface注释的接口，满足@FunctionalInterface注释的约束。

2、没有被@FunctionalInterface注释的接口，但是满足@FunctionalInterface注释的约束

 @FunctionalInterface注释的约束：

1、接口有且只能有个一个抽象方法，只有方法定义，没有方法体

2、在接口中覆写Object类中的public方法，不算是函数式接口的方法。

```

@FunctionalInterface
public interface FunctionInterfaceTest {
 
	String getInfo(String input);
	
	@Override
	String toString();  //Object中的方法
	
	@Override
	boolean equals(Object obj); //Object中的方法
}
//接口二
@FunctionalInterface
public interface FunctionInterfaceTest {
 
	String getInfo(String input);
	 
}

//接口三
public interface FunctionInterfaceTest {
 
	String getInfo(String input);
	 
}

```


函数式接口实例的创建

函数式接口实例的创建有三种方式：1、lambda表达式；2、方法引用；3、构造方法引用。

```
public class Main {
 
	 public static void main(String[] args) {
		
	       /**
	  	* 1、lambda表达式
	  	* 这种形式最为直观，lambda表达式，接收一个String类型的参数，返回一个String类型的结果。
	  	* 完全符合函数式接口FunctionInterfaceTest的定义
	  	*/
		FunctionInterfaceTest functionInterfaceTest1 = item -> item+1;  
		
		/**
		 * 2、方法引用
		 * Main方法当中的getInstance和getMessage方法接收一个参数，返回一个结果。符合函数式接口
		 * FunctionInterfaceTest的定义。
		 * 函数式接口只是定义了个方法的约定（接收一个String类型的参数，返回一个String类型的结果），
		 * 而对于方法内部进行何种操作则并没有做任何的限制。在这点上，跟java以前的版本中的实现类与接口之间的
		 * 关系很类似。不同的是，函数式接口更偏重于计算过程，约束了一个计算过程的输入和输出。
		 * 这种约束计算过程的输入和输出的形式的好处可以看一下joinStr方法。
		 */
		FunctionInterfaceTest functionInterfaceTest2 = Main::getInstance;  //方法引用
		FunctionInterfaceTest functionInterfaceTest3 = Main::getMessage;  //方法引用
		
		String msg1 = joinStr("你好",functionInterfaceTest2); //输出：你好！世界
		String msg2 = joinStr("你好",functionInterfaceTest3); //输出：世界，你好！
		System.out.println(msg1);
		System.out.println(msg2);
		
		//还有更简单的写法,高度抽象化，具体处理由使用者自己决定
		String msg3 = joinStr("你好",item ->item+"！世界"); //输出：你好！世界
		String msg4 = joinStr("你好",item ->"世界,"+ item+"!"); //输出：世界，你好！
		System.out.println(msg3);
		System.out.println(msg4);
		
		/**
		 * 3、构造方法引用
		 * 构造函数的结构：接收输入参数，然后返回一个对象。这种约束跟函数式接口的约束很像。
		 * 所以只要“输入参数类型”与“输出参数类型”跟FunctionInterfaceTest中的方法约束相同，
		 * 就可以创建出FunctionInterfaceTest接口的实例，如下，String的构造方法中有
		 * new String(str)的构造方法，所以可以得到实例。
		 * 这里存在一个类型推断的问题，JDK的编译器已经帮我们自动找到了只有一个参数，且是String类型的构造方法。
		 * 这就是我们直接String::new，没有指定使用哪一个构造方法，却可以创建实例的原因
		 */
		FunctionInterfaceTest functionInterfaceTest4 = String::new; //方法引用
	 }
	 
	 public static String getInstance(String item){
		 return item+"！世界";
	 }
	 
	 public static String getMessage(String massage){
		 return "世界,"+ massage+"!";
	 }
	 
	 public  static String joinStr(String str,FunctionInterfaceTest functionTest){
		 return functionTest.getInfo(str);



```


Java8中常用的函数式接口：

常用的函数式接口主要有四种类型，是通过其输入和输出的参数来进行区分的。定义了编码过程中主要的使用场景。

* Function<T,R>   :  接收一个T类型的参数，返回一个R类型的结果
* Consumer<T> : 接收一个T类型的参数，不返回值
* Predicate<T> : 接收一个T类型的参数，返回一个boolean类型的结果
* Supplier<T> :不接受参数，返回一个T类型的结果


```

public class FunctionalInterfaceMain {
 
	public static void main(String[] args) {
		/**
		 * 先看看如何创建它们
		 */
		Function<String,String> function1 = item -> item +"返回值";
		
		Consumer<String> function2 = iterm -> {System.out.println(iterm);};//lambda语句，使用大括号，没有return关键字，表示没有返回值
		
		Predicate<String> function3 = iterm -> "".equals(iterm);
		
		Supplier<String> function4 = () -> new String("");
		
		/**
		 * 再看看怎么使用
		 * demo释义：
		 * 1、创建一个String类型的集合
		 * 2、将集合中的所有元素的末尾追加字符串'1'
		 * 3、选出长度大于2的字符串
		 * 4、遍历输出所有元素
		 */
		List<String> list = Arrays.asList("zhangsan","lisi","wangwu","xiaoming","zhaoliu");
		
		list.stream()
			.map(value -> value + "1") //传入的是一个Function函数式接口
			.filter(value -> value.length() > 2) //传入的是一个Predicate函数式接口
			.forEach(value -> System.out.println(value)); //传入的是一个Consumer函数式接口
	}
	
}



```



Java8中对于接收两个参数的场景提供了相关的函数式接口。如下：

* BiFunction<T, U, R>   ：接收T类型和U类型的两个参数，返回一个R类型的结果
* BiConsumer<T , U>： 接收T类型和U类型的两个参数，不返回值
* BiPredicate<T, U> ：接收T类型和U类型的两个参数，返回一个boolean类型的结果

Function接口的andThen方法和compose方法

* Compose方法：方法接收一个Function类型的参数，返回一个值。这也是一个标准的Function类型的定义。在compose方法内部也有一个apply方法。在执行compose方法中的apply方法之前，它先执行了before接口的apply方法，也是compose方法的输入参数。然后将before方法执行的返回值作为compose中apply方法的输入参数。实际上是形成了一种链式组合。

* andThen方法：该方法与compose方法很类似。不同之处在于，andThen是先执行自身的apply方法，将apply的返回值作为after接口的输入值。相对于compose方法，只是方向的不同



```
default <V> Function<V, R> compose(Function<? super V, ? extends T> before) {
        Objects.requireNonNull(before);
        return (V v) -> apply(before.apply(v));
}
 
default <V> Function<T, V> andThen(Function<? super R, ? extends V> after) {
        Objects.requireNonNull(after);
        return (T t) -> after.apply(apply(t));

```

Consumer接口的andThen方法

将输入参数分别赋给andThen内部的accept方法和after内部的accept方法。After的计算在andThen之后，起到了后置连接的作用。在这里没有compose方法，因为后置连接反过来就是前置连接，所以不需要一个多余的compose方法了。只需要在传递时，交换两个consumer的顺序即可。


Predicate接口的and、or、negate方法

分别是&&, || 和取反操作。

此外，java8针对原生类型int，long，double都提供了相应的函数式接口。如：DoubleConsumer， DoubleFunction，IntConsumer等等，使用方式都相同，见java.util.function包。


