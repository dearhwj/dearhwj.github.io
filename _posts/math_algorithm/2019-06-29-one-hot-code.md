---
layout: post
title:  独热编码
category: 数学和算法
keywords: 
---

## 什么是独热编码

[原文地址:https://www.imooc.com/article/35900](https://www.imooc.com/article/35900)

One-Hot编码，又称为一位有效编码，主要是采用N位状态寄存器来对N个状态进行编码，每个状态都由他独立的寄存器位，并且在任意时候只有一位有效。

One-Hot编码是分类变量作为二进制向量的表示。这首先要求将分类值映射到整数值。然后，每个整数值被表示为二进制向量，除了整数的索引之外，它都是零值，它被标记为1。


就拿上面的例子来说吧，性别特征：["男","女"]，按照N位状态寄存器来对N个状态进行编码的原理，咱们处理后应该是这样的（这里只有两个特征，所以N=2）：

男  =>  10

女  =>  01

祖国特征：["中国"，"美国，"法国"]（这里N=3）：

中国  =>  100

美国  =>  010

法国  =>  001

运动特征：["足球"，"篮球"，"羽毛球"，"乒乓球"]（这里N=4）：

足球  =>  1000

篮球  =>  0100

羽毛球  =>  0010

乒乓球  =>  0001

所以，当一个样本为["男","中国","乒乓球"]的时候，完整的特征数字化的结果为：

[1，0，1，0，0，0，0，0，1]

## One-Hot在python中的使用

```
from sklearn import preprocessing  
  
enc = preprocessing.OneHotEncoder()  
enc.fit([[0,0,3],[1,1,0],[0,2,1],[1,0,2]])  #这里一共有4个数据，3种特征
array = enc.transform([[0,1,3]]).toarray()  #这里使用一个新的数据来测试   
print array   # [[ 1  0  0  1  0  0  0  0  1]]

```
结果为 1 0 0 1 0 0 0 0 1

## 为什么使用one-hot编码来处理离散型特征?


比如，有一个离散型特征，代表工作类型，该离散型特征，共有三个取值，不使用one-hot编码，其表示分别是x_1 = (1), x_2 = (2), x_3 = (3)。两个工作之间的距离是，(x_1, x_2) = 1, d(x_2, x_3) = 1, d(x_1, x_3) = 2。那么x_1和x_3工作之间就越不相似吗？显然这样的表示，计算出来的特征的距离是不合理。那如果使用one-hot编码，则得到x_1 = (1, 0, 0), x_2 = (0, 1, 0), x_3 = (0, 0, 1)，那么两个工作之间的距离就都是sqrt(2).即每两个工作之间的距离是一样的，显得更合理。

## 不需要使用one-hot编码来处理的情况

将离散型特征进行one-hot编码的作用，是为了让距离计算更合理，但如果特征是离散的，并且不用one-hot编码就可以很合理的计算出距离，那么就没必要进行one-hot编码。

比如，该离散特征共有1000个取值，我们分成两组，分别是400和600,两个小组之间的距离有合适的定义，组内的距离也有合适的定义，那就没必要用one-hot 编码。

离散特征进行one-hot编码后，编码后的特征，其实每一维度的特征都可以看做是连续的特征。就可以跟对连续型特征的归一化方法一样，对每一维特征进行归一化。比如归一化到[-1,1]或归一化到均值为0,方差为1。


