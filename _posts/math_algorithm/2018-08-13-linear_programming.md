---
layout: post
title: 线性规划
category: 数学和算法
keywords: 线性规划
---


## 线性规划3要素
我们总结线性规划模型的三要素如下： 

* 决策变量：需要决策的量， 即待求的未知变量； 
* 目标函数：需要优化的量， 即欲达的目标，用决策变量的线性式子表示； 
* 约束条件：为实现优化目标需要受到的限制， 用决策变量的等式或不等式表示．



## 线性规划实例

```

例 1 某机床厂生产甲、 乙两种机床， 每台销售后的利润分别为 4000 元与 3000 元。
生产甲机床需用 A、 B 机器加工，加工时间分别为每台 2 小时和 1 小时；生产乙机床
需用 A、 B、 C 三种机器加工，加工时间为每台各一小时。若每天可用于加工的机器时
数分别为 A 机器 10 小时、 B 机器 8 小时和C 机器 7 小时，问该厂应生产甲、乙机床各
几台，才能使总利润最大？
上述问题的数学模型： 设该厂生产 x1 台甲机床和 x2 乙机床时总利润最大， 则 x1, x2



```

![](https://img-blog.csdn.net/20180531105848847)  

这里变量 x1, x2 称之为决策变量

* (1) 式被称为问题的目标函数
* (2) 中的几个不等式  

是问题的约束条件，记为 s.t.(即 subject to)。由于上面的目标函数及约束条件均为线性  
函数，故被称为线性规划问题。