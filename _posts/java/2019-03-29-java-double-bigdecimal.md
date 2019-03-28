---
layout: post
title: Java中double转BigDecimal的注意事项
category: 
keywords: BigDecimal, double
---

## 正文
[原文地址:https://blog.csdn.net/lkforce/article/details/81564927](https://blog.csdn.net/lkforce/article/details/81564927)

1. BigDecimal(double val)构造，用double当参数来构造一个BigDecimal对象。

2. 但是这个构造不太靠谱(unpredictable)，你可能以为BigDecimal(0.1)就是妥妥的等于0.1，但是你以为你以为的就是你以为的？还真不是，BigDecimal(0.1)这货实际上等于0.1000000000000000055511151231257827021181583404541015625，因为准确的来说0.1本身不能算是一个double（其实0.1不能代表任何一个定长二进制分数）。

3. BigDecimal(String val)构造是靠谱的，BigDecimal(“0.1”)就是妥妥的等于0.1，推荐大家用这个构造。

4. 如果你非得用一个double变量来构造一个BigDecimal，没问题，我们贴心的提供了静态方法valueOf(double)，这个方法跟new Decimal(Double.toString(double))效果是一样的。
