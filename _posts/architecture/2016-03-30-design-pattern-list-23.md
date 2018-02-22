---
layout: post
title: 23种经典设计模式
category: 软件架构和设计
keywords: 设计模式
---



俗话说“熟读唐诗三百首 不会吟诗也会吟”，***把每种模式都操练过，当实际编码遇到问题的时候就把这23种模式拿出来，看看哪个套上去更顺眼就用哪个***......

### 创建型

* Factory Method（工厂方法）:参考[http://www.runoob.com/design-pattern/factory-pattern.html](http://www.runoob.com/design-pattern/factory-pattern.html)

* Abstract Factory（抽象工厂）:参考[http://www.runoob.com/design-pattern/abstract-factory-pattern.html](http://www.runoob.com/design-pattern/abstract-factory-pattern.html)
	* 抽象工厂模式和工厂模式的区别:[https://www.zhihu.com/question/20367734](https://www.zhihu.com/question/20367734)
 

* Builder（建造者）

* Prototype（原型）：原型模式是一个经典的GOF创建型模式，和其他的创建型模式（单例模式、工厂方法、抽象工厂和创建者）相似，原型模式也与对象创建有关，但是也有一个不同。使用原型模式，你不用为每一个客户端请求对象创建一个新的对象。相反，你首先创建一个对象叫做原型，并且为每一个客户端请求的对象产生一个副本。在java中，这是通过对象克隆,一种通过产生一个具有相同状态对象的副本作为原始对象的方式。

* Singleton（单例）：
	* [Java单例模式(Singleton)以及实现](https://www.cnblogs.com/cielosun/p/6582333.html)




### 结构型

* Adapter Class/Object（适配器）：在计算机编程中，适配器模式（有时候也称包装样式或者包装）将一个类的接口适配成用户所期待的。一个适配允许通常因为接口不兼容而不能在一起工作的类工作在一起，做法是将类自己的接口包裹在一个已存在的类中。共有两类适配器模式：对象适配器模式、类适配器模式。
	* [http://blog.csdn.net/yangjiachang1203/article/details/52484797](http://blog.csdn.net/yangjiachang1203/article/details/52484797) 	
*  Bridge（桥接）：Bridge 模式把两个角色之间的继承关系改为了耦合的关系，从而使这两者可以从容自若的各自独立的变化，这也是Bridge模式的本意[设计模式（六）桥连模式Bridge（结构型）](http://blog.csdn.net/hguisu/article/details/7529194)
	
	例如：现需要提供大中小3种型号的画笔，能够绘制5种不同颜色，如果使用蜡笔，我们需要准备3*5=15支蜡笔，也就是说必须准备15个具体的蜡笔类。而如果使用毛笔的话，只需要3种型号的毛笔，外加5个颜料盒，用3+5=8个类就可以实现15支蜡笔的功能。实际上，蜡笔和毛笔的关键一个区别就在于笔和颜色是否能够分离。即将抽象化(Abstraction)与实现化(Implementation)脱耦，使得二者可以独立地变化"。关键就在于能否脱耦。蜡笔的颜色和蜡笔本身是分不开的，所以就造成必须使用15支色彩、大小各异的蜡笔来绘制图画。而毛笔与颜料能够很好的脱耦，各自独立变化，便简化了操作。在这里，抽象层面的概念是："毛笔用颜料作画"，而在实现时，毛笔有大中小三号，颜料有红绿蓝黑白等5种，于是便可出现3×5种组合。每个参与者（毛笔与颜料）都可以在自己的自由度上随意转换。蜡笔由于无法将笔与颜色分离，造成笔与颜色两个自由度无法单独变化，使得只有创建15种对象才能完成任务。  

* Composite（组合）
	* [https://www.cnblogs.com/gaochundong/p/design_pattern_composite.html](https://www.cnblogs.com/gaochundong/p/design_pattern_composite.html) 

* Decorator（装饰）: [装饰器模式(Decorator)——深入理解与实战应用](https://www.cnblogs.com/jzb-blog/p/6717349.html)

	* 适配器 vs 代理模式：适配器改变所考虑的对象的接口，代理模式不能改变所代理对象的接口
	* 装饰器 vs 代理模式：	装饰器为所装饰的对象提供增强功能，代理模式对对象的使用施加控制，不提供对象本身的增强功能
	* 适配器 vs 装饰器模式：都是包装模式，适配器把一个API转换成另一个API，装饰器保存被包装的对象的API



* Facade（外观）:[https://www.jianshu.com/p/1b027d9fc005](https://www.jianshu.com/p/1b027d9fc005)
	* 与适配器模式的区别
		* 外观模式的实现核心主要是——由外观类去保存各个子系统的引用，实现由一个统一的外观类去包装多个子系统类，然而客户端只需要引用这个外观类，然后由外观类来调用各个子系统中的方法。
		* 这样的实现方式非常类似适配器模式，然而外观模式与适配器模式不同的是：适配器模式是将一个对象包装起来以改变其接口，而外观是将一群对象 ”包装“起来以简化其接口。它们的意图是不一样的，适配器是将接口转换为不同接口，而外观模式是提供一个统一的接口来简化接口。


* Flyweight（享元）
	* [http://www.runoob.com/design-pattern/flyweight-pattern.html](http://www.runoob.com/design-pattern/flyweight-pattern.html)
	* [http://blog.csdn.net/justloveyou_/article/details/55045638](http://blog.csdn.net/justloveyou_/article/details/55045638)
* Proxy（代理）
	* [Java的三种代理模式](https://www.cnblogs.com/cenyu/p/6289209.html) 

### 行为型

* Interpreter（解释器）
	* [https://www.2cto.com/kf/201606/520405.html](https://www.2cto.com/kf/201606/520405.html)

* Template Method（模板方法）:实现一些操作时，整体步骤很固定，但是呢。就是其中一小部分容易变，这时候可以使用模板方法模式，将容易变的部分抽象出来，供子类实现。
	* [https://www.cnblogs.com/meet/p/5116417.html](https://www.cnblogs.com/meet/p/5116417.html) 

* Chain of Responsibility（责任链）

16. Command（命令）

17. Iterator（迭代器）

18. Mediator（中介者）

19. Memento（备忘录）

20. Observer（观察者）

21. State（状态）

22. Strategy（策略）

23. Visitor（访问者）


### 参考资料
[http://www.runoob.com/design-pattern/design-pattern-tutorial.html](http://www.runoob.com/design-pattern/design-pattern-tutorial.html)