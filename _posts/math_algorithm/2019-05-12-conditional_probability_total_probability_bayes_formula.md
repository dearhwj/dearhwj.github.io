---
layout: post
title: 条件概率公式&全概率公式&贝叶斯公式
category: 数学和算法
keywords: 条件概率,全概率,贝叶斯
---
## 条件概率公式

设A,B是两个事件，且P(B)>0,则在事件B发生的条件下，事件A发生的条件概率（conditional probability)为：

	P(A|B)=P(AB)/P(B)

## 乘法公式

1.由条件概率公式得：

	P(AB)=P(A|B)P(B)=P(B|A)P(A)    

上式即为乘法公式；

2.乘法公式的推广：对于任何正整数n≥2，当P(A<sub>1</sub>A<sub>2</sub>...A<sub>n-1</sub>) > 0 时，有：

P(A<sub>1</sub>A<sub>2</sub>...A<sub>n-1</sub>A<sub>n</sub>)=P(A<sub>1</sub>)P(A<sub>2</sub>|A<sub>1</sub>)P(A<sub>3</sub>|A<sub>1</sub>A<sub>2</sub>)...P(A<sub>n</sub>|A<sub>1</sub>A<sub>2</sub>...A<sub>n-1</sub>)

## 全概率公式

1. 如果事件组B<sub>1</sub>，B<sub>2</sub>，.... 满足

	1. B<sub>1</sub>，B<sub>2</sub>....两两互斥，即 B<sub>i </sub>∩ B<sub>j </sub>= ∅ ，i≠j ， i,j=1，2，....，且P(B<sub>i</sub>)>0,i=1,2,....;

	2. B<sub>1</sub>∪B<sub>2</sub>∪....=Ω ，则称事件组 B<sub>1</sub>,B<sub>2</sub>,...是样本空间Ω的一个划分

设 B<sub>1</sub>,B<sub>2</sub>,...是样本空间Ω的一个划分，A为任一事件，则：

![](https://images2015.cnblogs.com/blog/953214/201606/953214-20160630111733843-1686464542.png)

上式即为全概率公式（formula of total probability)

2. 全概率公式的意义在于，当直接计算P(A)较为困难,而P(B<sub>i</sub>),P(A|B<sub>i</sub>)  (i=1,2,...)的计算较为简单时，可以利用全概率公式计算P(A)。思想就是，将事件A分解成几个小事件，通过求小事件的概率，然后相加从而求得事件A的概率，而将事件A进行分割的时候，不是直接对A进行分割，而是先找到样本空间Ω的一个个划分B<sub>1</sub>,B<sub>2</sub>,...B<sub>n</sub>,这样事件A就被事件AB<sub>1</sub>,AB<sub>2</sub>,...AB<sub>n</sub>分解成了n部分，即A=AB<sub>1</sub>+AB<sub>2</sub>+...+AB<sub>n</sub>, 每一B<sub>i</sub>发生都可能导致A发生相应的概率是P(A|B<sub>i</sub>)，由加法公式得

P(A)=P(AB<sub>1</sub>)+P(AB<sub>2</sub>)+....+P(AB<sub>n</sub>)

=P(A|B<sub>1</sub>)P(B<sub>1</sub>)+P(A|B<sub>2</sub>)P(B<sub>2</sub>)+...+P(A|B<sub>n</sub>)P(PB<sub>n</sub>)

3.实例：某车间用甲、乙、丙三台机床进行生产，各台机床次品率分别为5%，4%，2%，它们各自的产品分别占总量的25%，35%，40%，将它们的产品混在一起，求任取一个产品是次品的概率。

解：设.....     P(A)=25%*5%+4%*35%+2%*40%=0.0345

## 贝叶斯公式

1.与全概率公式解决的问题相反，贝叶斯公式是建立在条件概率的基础上寻找事件发生的原因（即大事件A已经发生的条件下，分割中的小事件Bi的概率），设B<sub>1</sub>,B<sub>2</sub>,...是样本空间Ω的一个划分，则对任一事件A（P(A)>0),有

![](/images/bayes_formula.png)

上式即为贝叶斯公式（Bayes formula)，B<sub>i </sub>常被视为导致试验结果A发生的”原因“，P(B<sub>i</sub>)(i=1,2,...)表示各种原因发生的可能性大小，故称先验概率；P(B<sub>i</sub>|A)(i=1,2...)则反映当试验产生了结果A之后，再对各种原因概率的新认识，故称后验概率。

2.实例：发报台分别以概率0.6和0.4发出信号“∪”和“—”。由于通信系统受到干扰，当发出信号“∪”时，收报台分别以概率0.8和0.2受到信号“∪”和“—”；又当发出信号“—”时，收报台分别以概率0.9和0.1收到信号“—”和“∪”。求当收报台收到信号“∪”时，发报台确系发出“∪”的概率。

解：设....， P(B<sub>1</sub>|A）= (0.6*0.8)/(0.6*0.8+0.4*0.1)=0.923