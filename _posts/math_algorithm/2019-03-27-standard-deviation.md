---
layout: post
title: 标准差公式
category: 数学和算法
keywords: 标准差
---

## 正文
[原文地址:https://baike.baidu.com/item/%E6%A0%87%E5%87%86%E5%B7%AE%E5%85%AC%E5%BC%8F/7238847](https://baike.baidu.com/item/%E6%A0%87%E5%87%86%E5%B7%AE%E5%85%AC%E5%BC%8F/7238847)

标准差公式是一种数学公式。标准差也被称为标准偏差，或者实验标准差，公式如下所示：
	
		标准差=方差的算术平方根
		s=sqrt(((x1-x)^2 +(x2-x)^2 +......(xn-x)^2)/n)。


简单来说，***标准差是一组数值自平均值分散开来的程度的一种测量观念。一个较大的标准差，代表大部分的数值和其平均值之间差异较大；一个较小的标准差，代表这些数值较接近平均值***。

例如，两组数的集合 {0, 5, 9, 14} 和 {5, 6, 8, 9} 其平均值都是 7 ，但第二个集合具有较小的标准差。

标准差可以当作不确定性的一种测量。例如在物理科学中，做重复性测量时，测量数值集合的标准差代表这些测量的精确度。当要决定测量值是否符合预测值，测量值的标准差占有决定性重要角色：如果测量平均值与预测值相差太远（同时与标准差数值做比较），则认为测量值与预测值互相矛盾。这很容易理解，因为如果测量值都落在一定数值范围之外，可以合理推论预测值是否正确。

标准差应用于投资上，可作为量度回报稳定性的指标。标准差数值越大，代表回报远离过去平均数值，回报较不稳定故风险越高。相反，标准差数值越小，代表回报较为稳定，风险亦较小。

例如，A、B两组各有6位学生参加同一次语文测验，A组的分数为95、85、75、65、55、45，B组的分数为73、72、71、69、68、67。这两组的平均数都是70，但A组的标准差为17.078分，B组的标准差为2.160分（此数据使用的是总本标准差），说明A组学生之间的差距要比B组学生之间的差距大得多。

如是总体，标准差公式根号内除以n

***如是样本，标准差公式根号内除以（n-1)。***

因为我们大量接触的是样本，所以普遍使用根号内除以（n-1)。

***公式意义***

所有数减去平均值，它的平方和除以数的个数（或个数减一)，再把所得值开根号，就是1/2次方，得到的数就是这组数的标准差。

标准差
由于方差是数据的平方，与检测值本身相差太大，人们难以直观的衡量，所以常用方差开根号换算回来这就是我们要说的标准差（SD）。
在统计学中样本的均差多是除以自由度（n-1)，它的意思是样本能自由选择的程度。当选到只剩一个时，它不可能再有自由了，所以自由度是（n-1)。


## 有了方差为什么需要标准差？
[参考资料:https://www.zhihu.com/question/20534502/answer/202286999](https://www.zhihu.com/question/20534502/answer/202286999)

