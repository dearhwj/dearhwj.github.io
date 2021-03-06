---
layout: post
title: 禁忌搜索算法
category: 数学和算法
keywords: 禁忌搜索,TABU
---

## 什么是禁忌搜索算法
[原文地址:https://www.cnblogs.com/infroad/p/9737556.html](https://www.cnblogs.com/infroad/p/9737556.html)
### 先从爬山算法说起
爬山算法从当前的节点开始，和周围的邻居节点的值进行比较。 如果当前节点是最大的，那么返回当前节点，作为最大值 (既山峰最高点)；反之就用最高的邻居节点来，替换当前节点，从而实现向山峰的高处攀爬的目的。如此循环直到达到最高点。因为不是全面搜索，所以结果可能不是最佳。

### 再到局部搜索算法
局部搜索算法是从爬山法改进而来的。局部搜索算法的基本思想：在搜索过程中，始终选择当前点的邻居中与离目标最近者的方向搜索。同样，局部搜索得到的解不一定是最优解。

### 然后到禁忌搜索算法
为了找到“全局最优解”，就不应该执着于某一个特定的区域。于是人们对局部搜索进行了改进，得出了禁忌搜索算法。

禁忌（Tabu Search）算法是一种亚启发式(meta-heuristic)随机搜索算法，它从一个初始可行解出发，选择一系列的特定搜索方向（移动）作为试探，选择实现让特定的目标函数值变化最多的移动。为了避免陷入局部最优解，TS搜索中采用了一种灵活的“记忆”技术，对已经进行的优化过程进行记录和选择，指导下一步的搜索方向，这就是Tabu表的建立。

### 最后打个比方
为了找出地球上最高的山，一群有志气的兔子们开始想办法。 
1. 爬山算法
兔子朝着比现在高的地方跳去。他们找到了不远处的最高山峰。但是这座山不一定是珠穆朗玛峰。这就是爬山法，它不能保证局部最优值就是全局最优值。

2. 禁忌搜索算法
兔子们知道一个兔的力量是渺小的。他们互相转告着，哪里的山已经找过，并且找过的每一座山他们都留下一只兔子做记号。他们制定了下一步去哪里寻找的策略。这就是禁忌搜索。

## 思想和过程
###  基本思想
标记已经解得的局部最优解或求解过程，并在进一步的迭代中避开这些局部最优解或求解过程。局部搜索的缺点在于，太过于对某一局部区域以及其邻域的搜索，导致一叶障目。为了找到全局最优解，禁忌搜索就是对于找到的一部分局部最优解，有意识地避开它，从而或得更多的搜索区域。

比喻：兔子们找到了泰山，它们之中的一只就会留守在这里，其他的再去别的地方寻找。就这样，一大圈后，把找到的几个山峰一比较，珠穆朗玛峰脱颖而出。

### 算法过程
1. step1：给以禁忌表H=空集，并选定一个初始解xnow；

2. step2：满足停止规则时，停止计算，输出结果；否则，在xnow的邻域N(xnow)中选择不受禁忌的候选集Can_N(xnow)；在Can_N(xnow)中选一个评价值最佳的解xnext，xnow=xnext；更新历史记录H，保存f(xnow)，重复step2；

3. step3：在保存的众多f中，挑选最小（大）值作为解；

### 相关概念解释
又到了科普时间了。其实，关于邻域的概念前面的好多博文都介绍过了。今天还是给大家介绍一下。这些概念对理解整个算法的意义很大，希望大家好好理解。

1. 邻域
官方一点：所谓邻域，简单的说即是给定点附近其他点的集合。在距离空间中，邻域一般被定义为以给定点为圆心的一个圆；而在组合优化问题中，邻域一般定义为由给定转化规则对给定的问题域上每结点进行转化所得到的问题域上结点的集合。
通俗一点：邻域就是指对当前解进行一个操作(这个操作可以称之为邻域动作)可以得到的所有解的集合。那么邻域的本质区别就在于邻域动作的不同了。

2. 邻域动作
邻域动作是一个函数，通过这个函数，对当前解s，产生其相应的邻居解集合。例如：对于一个bool型问题，其当前解为：s = 1001，当将邻域动作定义为翻转其中一个bit时，得到的邻居解的集合N(s)={0001,1101,1011,1000}，其中N(s) ∈ S。同理，当将邻域动作定义为互换相邻bit时，得到的邻居解的集合N(s)={0101,1001,1010}。

3. 禁忌表
包括禁忌对象和禁忌长度。（当兔子们再寻找的时候，一般地会有意识地避开泰山，因为他们知道，这里已经找过，并且有一只兔子在那里看着了。这就是禁忌搜索中“禁忌表（tabu list）”的含义。）

4. 侯选集合
侯选集合由邻域中的邻居组成。常规的方法是从邻域中选择若干个目标值或评价值最佳的邻居入选。

5. 禁忌对象
禁忌算法中，由于我们要避免一些操作的重复进行，就要将一些元素放到禁忌表中以禁止对这些元素进行操作，这些元素就是我们指的禁忌对象。（当兔子们再寻找的时候，一般地会有意识地避开泰山，因为这里找过了。并且还有一只兔子在这留守。）

6. 禁忌长度
禁忌长度是被禁对象不允许选取的迭代次数。一般是给被禁对象x一个数（禁忌长度） t ，要求对象x 在t 步迭代内被禁，在禁忌表中采用tabu(x)=t记忆，每迭代一步，该项指标做运算tabu(x)=t−1，直到tabu(x)=0时解禁。于是，我们可将所有元素分成两类，被禁元素和自由元素。禁忌长度t 的选取可以有多种方法，例如t=常数，或t=[√n]，其中n为邻域中邻居的个数；这种规则容易在算法中实现。
（那只留在泰山的兔子一般不会就安家在那里了，它会在一定时间后重新回到找最高峰的大军，因为这个时候已经有了许多新的消息，泰山毕竟也有一个不错的高度，需要重新考虑，这个归队时间，在禁忌搜索里面叫做“禁忌长度（tabu length）”。）

7. 评价函数
评价函数是侯选集合元素选取的一个评价公式，侯选集合的元素通过评价函数值来选取。以目标函数作为评价函数是比较容易理解的。目标值是一个非常直观的指标，但有时为了方便或易于计算，会采用其他函数来取代目标函数。

8. 特赦规则
在禁忌搜索算法的迭代过程中，会出现侯选集中的全部对象都被禁忌，或有一对象被禁，但若解禁则其目标值将有非常大的下降情况。在这样的情况下，为了达到全局最优，我们会让一些禁忌对象重新可选。这种方法称为特赦，相应的规则称为特赦规则。
（如果在搜索的过程中，留守泰山的兔子还没有归队，但是找到的地方全是华北平原等比较低的地方，兔子们就不得不再次考虑选中泰山，也就是说，当一个有兔子留守的地方优越性太突出，超过了“best so far”的状态，就可以不顾及有没有兔子留守，都把这个地方考虑进来，这就叫“特赦准则（aspiration criterion）”。）