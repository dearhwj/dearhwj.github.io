---
layout: post
title: 生长曲线(S曲线)预测法
category: 数学和算法
keywords: S曲线,生长曲线
---
## 正文
[原文地址:https://wiki.mbalib.com/wiki/%E7%94%9F%E9%95%BF%E6%9B%B2%E7%BA%BF%28S%E6%9B%B2%E7%BA%BF%29%E9%A2%84%E6%B5%8B%E6%B3%95](https://wiki.mbalib.com/wiki/%E7%94%9F%E9%95%BF%E6%9B%B2%E7%BA%BF%28S%E6%9B%B2%E7%BA%BF%29%E9%A2%84%E6%B5%8B%E6%B3%95)


### 什么是生长曲线(S曲线)预测法
　　生长曲线预测法也称生长曲线模型（Growth curve models）是预测事件的一组观测数据随时间的变化符合生长曲线的规律，以生长曲线模型进行预测的方法。一般来说，事物总是经过发生、发展、成熟三个阶段，而每一个阶段的发展速度各不相同。通常在发生阶段，变化速度较为缓慢；在发展阶段，变化速度加快；在成熟阶段，变化速度又趋缓慢，按上述三个阶段发展规律得到的变化曲线称为生长曲线。



### 皮尔模型
皮尔生长曲线的一般模型为

![https://wiki.mbalib.com/w/images/math/f/9/d/f9def4566ee02f09cf437db415e7682b.png](https://wiki.mbalib.com/w/images/math/f/9/d/f9def4566ee02f09cf437db415e7682b.png)

式中，K为常数(如某种耐用消费品饱和状态时的普及率)；

​	![https://wiki.mbalib.com/w/images/math/d/7/0/d704c8f86aa98e65ca6ef051239e2de8.png](https://wiki.mbalib.com/w/images/math/d/7/0/d704c8f86aa98e65ca6ef051239e2de8.png)

　　常用的皮尔生长曲线模型为

​	![https://wiki.mbalib.com/w/images/math/1/4/8/14867ea0b5802df4214e5f84ef6a2ddc.png](https://wiki.mbalib.com/w/images/math/1/4/8/14867ea0b5802df4214e5f84ef6a2ddc.png)

　　这时f(x)是x的线性函数，且具有负斜率。见下图是皮尔曲线模型的图。

![https://wiki.mbalib.com/w/images/5/51/%E7%9A%AE%E5%B0%94%E6%9B%B2%E7%BA%BF%E6%A8%A1%E5%9E%8B%E7%9A%84%E5%9B%BE.jpg](https://wiki.mbalib.com/w/images/5/51/%E7%9A%AE%E5%B0%94%E6%9B%B2%E7%BA%BF%E6%A8%A1%E5%9E%8B%E7%9A%84%E5%9B%BE.jpg)

### 林德诺模型
　　常用于新技术发展和新产品销售的一种预测方法。

### 龚帕兹模型
　　龚帕兹(生长)曲线是一种常用曲线，其形式为

![https://wiki.mbalib.com/w/images/math/5/4/a/54a6addef2d3d912bac1dbec88a6b85f.png](https://wiki.mbalib.com/w/images/math/5/4/a/54a6addef2d3d912bac1dbec88a6b85f.png)
　　K＞0，a＜1，0＜b＜1　　(11)

　　对参数a、b、K的不同取值，龚帕兹模型有不同的形状和变化趋势。图(a)为1n a＜0，0＜b＜l时的龚帕兹曲线；图(b)为1n a＜0，b＞1时的曲线；图(c)为1n a＞0，0＜b＜1时的曲线；图(d)为ln a＞0，b＞1时的曲线。

![https://wiki.mbalib.com/w/images/3/3e/%E9%BE%9A%E5%B8%95%E5%85%B9%28%E7%94%9F%E9%95%BF%29%E6%9B%B2%E7%BA%BF.jpg](https://wiki.mbalib.com/w/images/3/3e/%E9%BE%9A%E5%B8%95%E5%85%B9%28%E7%94%9F%E9%95%BF%29%E6%9B%B2%E7%BA%BF.jpg)

　　给定时间序列![https://wiki.mbalib.com/w/images/math/8/8/a/88ace46a820d7448e5f65b6e95533a14.png](https://wiki.mbalib.com/w/images/math/8/8/a/88ace46a820d7448e5f65b6e95533a14.png)只要求得其中的三个参数值a、b、K，就可以用来求得未来周期的预测值。

　　求参数a、b、K的方法有多种，如非线性回归分析、特殊函数的最小二乘法等。这里介绍一种比较简单的方法，其步骤如下：

　　(1)将N个数据分成三组(这里假设N=3r)；

　　(2)求各组的yi值的对数和，即求：

![https://wiki.mbalib.com/w/images/math/9/b/2/9b257f919cba99532653888008ab02a7.png](https://wiki.mbalib.com/w/images/math/9/b/2/9b257f919cba99532653888008ab02a7.png)

　　(3)利用下列公式计算参数a、b、K的值；

![https://wiki.mbalib.com/w/images/math/e/e/a/eea2cb20970b5bb9828dc397d82741cb.png](https://wiki.mbalib.com/w/images/math/e/e/a/eea2cb20970b5bb9828dc397d82741cb.png)

![https://wiki.mbalib.com/w/images/math/c/c/4/cc4a16c0fae4563dd190063b2d28dd93.png](https://wiki.mbalib.com/w/images/math/c/c/4/cc4a16c0fae4563dd190063b2d28dd93.png)

![https://wiki.mbalib.com/w/images/math/8/8/e/88eca82ec56674feccf4a17011fd514a.png](https://wiki.mbalib.com/w/images/math/8/8/e/88eca82ec56674feccf4a17011fd514a.png)

　　(4)直接计算K值的公式为

h![ttps://wiki.mbalib.com/w/images/math/8/c/5/8c54e91c9124e278d933b82357139bc6.png](ttps://wiki.mbalib.com/w/images/math/8/c/5/8c54e91c9124e278d933b82357139bc6.png)


