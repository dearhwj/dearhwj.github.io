---
layout: post
title: 标准正态分布概率表
category: 数学和算法
keywords: 标准正态,标准正态分布概率表
---

## 标准正态分布概率表

![](http://img.blog.csdn.net/20140902170029542?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemhhbmdob25neGlhbjEyMw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



![](http://img.blog.csdn.net/20140902170132093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemhhbmdob25neGlhbjEyMw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

该表计算的是：P(X<=x)【**某个数落在某个[-@,x]**】的概率。也就是下面阴影图形所示的面积：

![](http://img.blog.csdn.net/20140902170929615?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemhhbmdob25neGlhbjEyMw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



## Z值的计算

Z 值是某一特征值与均值之间标准偏差的数量，其是一个相对量。
Z 值的计算公式为：

![](/images/z_formula.png)



例如，对于某组成绩组数据，服从平均值为45，标准差是10的正态分布：


那么，任抽取一个同学的成绩，它的分数在63以上的概率为多少【落在[63,+@]区间的概率】？

也就是图中斜线的面积！

如果对f(x)做-@到63的计分，在用1减去它。计分比较麻烦。那么，将组数据标准化，标准化后的数据服从标准整体分布~！就将63数据标准化。

对63标准化就是“距离/标准差”

（63-45）/10=1.8。就是说，在标准整体分布中，得分落在区间[1.8,+@]的概率是：

1-0.9641=0.0359=3.59%

也就说，对于正态分布，想求得数据区间概率（面积），将“分割点”标准化即可，查表即可！！

以下描述是等同的：

全体学生，分数超过63分的同学占3.59%；

全体学生，任取一个分数大于63分的概率为3.59%；

全体学生，任取一个分数，标准计分大于1.8的概率为3.59%；


### 参考资料
[https://www.cnblogs.com/yanjunhelloworld/p/4844741.html](https://www.cnblogs.com/yanjunhelloworld/p/4844741.html)