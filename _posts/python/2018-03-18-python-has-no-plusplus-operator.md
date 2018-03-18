---
keywords: Python
layout: post
title: python 没有++运算符，这个事情原来不像仅仅是没有这个运算符那么简单
category: Python
---
 
## 正文
原文地址[http://blog.csdn.net/somehow1002/article/details/73744626](http://blog.csdn.net/somehow1002/article/details/73744626)
 
python 中，变量是以内容为基准而不是像 c 中以变量名为基准，所以只要你的数字内容是5，不管你起什么名字，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问
这样的设计逻辑决定了 python 中数字类型的值是不可变的，因为如果如上例，a 和 b 都是 5，当你改变了 a 时，b 也会跟着变，这当然不是我们希望的

因此，正确的自增操作应该 a = a + 1 或者 a += 1，当此 a 自增后，通过 id() 观察可知，id 值变化了，即 a 已经是新值的名称