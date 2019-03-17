---
layout: post
title:  整数规划
category: 数学和算法
---

## 整数规划

[原文地址:https://blog.csdn.net/bqw18744018044/article/details/79605544](https://blog.csdn.net/bqw18744018044/article/details/79605544)

对决策变量有整数要求的数学规划问题称为整数规划。

 

## 整数规划分类
* 全整数规划：所有决策变量取整数值；
* 0-1整数规划：整数变量只能取0或1；
* 混合整数规划：部分决策变量取整数值；

 

##  案例一

1. 一个社区理事会要决定在社区建设哪种娱乐设施，有四中备选方案：游泳池、网球场、运动场、健身房。理事会希望建立的设施使居民的预期日使用量最大。每个设施的预期日使用量和成本约束条件如表。

**娱乐设施** | **预期使用****（人/天）** | **成本****$** | **土地需求****（英亩）** | **决策变量**
-------- | ------------------- | ------------- | ------------------ | --------
游泳池      | 300                 | 35000         | 4                  | x1      
网球场      | 90                  | 10000         | 2                  | x2      
运动场      | 400                 | 25000         | 7                  | x3      
健身房      | 150                 | 90000         | 3                  | x4      
 

理事会有120000美元的建设预算和12英亩土地。游泳池和网球场只能建一个，理事会如何建设娱乐设施组合能最大化预期使用量。

 

2. 线性规划模型

决策变量依次表示对应的娱乐设施是否建立。取值为0表示不建设，取值为1则表示建设。

![](https://img-blog.csdn.net/20180318222754869?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 

3.      使用EXCEL求解

![](https://img-blog.csdn.net/20180318222815894?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



![](https://img-blog.csdn.net/20180318222821673?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
 
4.      其他可能的约束类型

![](https://img-blog.csdn.net/2018031822285529?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
 

四、       案例二

1.      某食品厂在西南部和中西部有种植和收获土豆的农场，然后把土豆运到A、B、C地方上的各个加工厂（共3个），在这些加工厂中生产包括薯条在内的不同种类的土豆产品。最近公司的产品需求量增加，因此该厂想买一个或者多个新农场来生产更多的土豆产品。公司正在考虑6个新的农场。他们的固定成本和预计产量如下表：


**农场** | **固定年成本（千美元）** | **预计年常量（千吨）**
------ | -------------- | -------------
1      | 405            | 11.2         
2      | 390            | 10.5         
3      | 450            | 12.8         
4      | 368            | 9.3          
5      | 520            | 10.8         
6      | 465            | 9.6          

 

三个工厂的剩余加工能力如下表：

**工厂** | **可用加工能力（千吨）**
------ | --------------
A      | 12            
B      | 10            
C      | 14            

 

从6个可能的农场地点向3个工厂运送土豆的单位成本如下表：

 
|**农场** | **加工厂运输成本（美元/吨）**|**加工厂运输成本（美元/吨）**|**加工厂运输成本（美元/吨）**|
------ | ----------------- | ----- | ---
  |**A**  | **B**             | **C**
1      | 18                | 15    | 12
2      | 13                | 10    | 17
3      | 16                | 14    | 18
4      | 19                | 15    | 16
5      | 17                | 19    | 12
6      | 14                | 16    | 12

 

公司应该购买哪几个农场能以最小的总成本满足可用的加工能力？（总成本包括固定成本和运输成本）

 

2.      线性规划模型



![](https://img-blog.csdn.net/20180318223107749?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/2018031822313953?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/20180318223210571?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2JxdzE4NzQ0MDE4MDQ0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  




