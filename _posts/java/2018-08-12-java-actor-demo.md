---
layout: post
title: Actor模型官方Java Demo
category: JAVA
keywords: Actor
---

## 生成Dem工程
通过[Lightbend Tech Hub ](https://developer.lightbend.com/start/?group=akka&project=akka-quickstart-java) 生成一个Demo用例，Demo工序可以用Java模式也可以用Scala模式，Demo用例可以直接下载。

## 理解Demo程序
	
	public class AkkaQuickstart {
	  public static void main(String[] args) {
	    final ActorSystem system = ActorSystem.create("helloakka");
	    try {
	      //#create-actors
	      final ActorRef printerActor = 
	        system.actorOf(Printer.props(), "printerActor");
	      final ActorRef howdyGreeter = 
	        system.actorOf(Greeter.props("Howdy", printerActor), "howdyGreeter");
	      final ActorRef helloGreeter = 
	        system.actorOf(Greeter.props("Hello", printerActor), "helloGreeter");
	      final ActorRef goodDayGreeter = 
	        system.actorOf(Greeter.props("Good day", printerActor), "goodDayGreeter");
	      //#create-actors
	
	      //#main-send-messages
	      howdyGreeter.tell(new WhoToGreet("Akka"), ActorRef.noSender());
	      howdyGreeter.tell(new Greet(), ActorRef.noSender());
	
	      howdyGreeter.tell(new WhoToGreet("Lightbend"), ActorRef.noSender());
	      howdyGreeter.tell(new Greet(), ActorRef.noSender());
	
	      helloGreeter.tell(new WhoToGreet("Java"), ActorRef.noSender());
	      helloGreeter.tell(new Greet(), ActorRef.noSender());
	
	      goodDayGreeter.tell(new WhoToGreet("Play"), ActorRef.noSender());
	      goodDayGreeter.tell(new Greet(), ActorRef.noSender());
	      //#main-send-messages
	
	      System.out.println(">>> Press ENTER to exit <<<");
	      System.in.read();
	    } catch (IOException ioe) {
	    } finally {
	      system.terminate();
	    }
	 }   
    
1. ActorSystem作为顶级Actor，可以创建和停止Actors,甚至可关闭整个Actor环境，
此外Actors是按层次划分的，ActorSystem就好比Java中的Object对象，Scala中的Any，
是所有Actors的根，当你通过ActorSystem的actof方法创建Actor时，实际就是在ActorSystem
下创建了一个子Actor。
2. 通过ActorSystem创建了1个Printer Actor的代理(ActorRef)和3个Greeter Actor
3. 发送消息给 Greeter Actor， Greeter Actor会立即存储消息，然后消息会给到Printer Actor，Printer Actor打印到Console。Akka就是利用这种异步的消息机制来获取大量的好处。

## 使用Actor Model模式的好处
1. 事件模型驱动–Actor之间的通信是异步的，即使Actor在发送消息后也无需阻塞或者等待就能够处理其他事情
2. 强隔离性–Actor中的方法不能由外部直接调用，所有的一切都通过消息传递进行的，从而避免了Actor之间的数据共享，想要观察到另一个Actor的状态变化只能通过消息传递进行询问
3. 位置透明–无论Actor地址是在本地还是在远程机上对于代码来说都是一样的
4. 轻量性–Actor是非常轻量的计算单机，单个Actor仅占400多字节，只需少量内存就能达到高并发

### 参考资料
[Actor模型原理](https://www.cnblogs.com/MOBIN/p/7236893.html)




