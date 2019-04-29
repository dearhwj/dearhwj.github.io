---
layout: post
title: 回归模型
category: 数学和算法
keywords: 异常点检测方法,离群点,离群点检测方法
---


## 什么是回归分析？

回归分析是一种预测建模技术的方法，研究因变量（目标）和自变量（预测器）之前的关系。这一技术被用在预测、时间序列模型和寻找变量之间因果关系。例如研究驾驶员鲁莽驾驶与交通事故发生频率之间的关系，就可以通过回归分析来解决。

回归分析是进行数据建模、分析的重要工具。下面这张图反映的是使用一条曲线来拟合离散数据点。其中，所有离散数据点与拟合曲线对应位置的差值之和是被最小化了的，更多细节我们会慢慢介绍。

![这里写图片描述](https://img-blog.csdn.net/20180719205527204?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 2. 为什么使用回归分析？

如上面所说，回归分析能估计两个或者多个变量之间的关系。下面我们通过一个简单的例子来理解：

比如说，你想根据当前的经济状况来估计一家公司的销售额增长。你有最近的公司数据，数据表明销售增长大约是经济增长的 2.5 倍。利用这种洞察力，我们就可以根据当前和过去的信息预测公司未来的销售情况。

使用回归模型有很多好处，例如：

1.  揭示了因变量和自变量之间的显著关系

2.  揭示了多个自变量对一个因变量的影响程度大小

回归分析还允许我们比较在不同尺度上测量的变量的影响，例如价格变化的影响和促销活动的数量的影响。这样的好处是可以帮助市场研究者 / 数据分析家 / 数据科学家评估选择最佳的变量集，用于建立预测模型。

## 3. 有哪些回归类型？

有许多回归技术可以用来做预测。这些回归技术主要由三个度量（独立变量的数量、度量变量的类型和回归线的形状）驱动。我们将在下面的章节中详细讨论。

![这里写图片描述](https://img-blog.csdn.net/20180719205648360?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

对于有创造力的人来说，可以对上面的参数进行组合，甚至创造出新的回归。但是在此之前，让我们来看一看最常见的几种回归。

### 1) 线性回归（Linear Regression）

线性回归是最为人熟知的建模技术，是人们学习如何预测模型时的首选之一。在此技术中，因变量是连续的，自变量可以是连续的也可以是离散的。回归的本质是线性的。

线性回归通过使用最佳的拟合直线（又被称为回归线），建立因变量（Y）和一个或多个自变量（X）之间的关系。

它的表达式为：Y=a+b*X+e，其中 a 为直线截距，b 为直线斜率，e 为误差项。如果给出了自变量 X，就能通过这个线性回归表达式计算出预测值，即因变量 Y。

![这里写图片描述](https://img-blog.csdn.net/20180719205744855?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

一元线性回归和多元线性回归的区别在于，多元线性回归有大于 1 个自变量，而一元线性回归只有 1 个自变量。接下来的问题是“如何获得最佳拟合直线？”

**如何获得最佳拟合直线（确定 a 和 b 值）？**

这个问题可以使用最小二乘法（Least Square Method）轻松解决。最小二乘法是一种拟合回归线的常用算法。它通过最小化每个数据点与预测直线的垂直误差的平方和来计算得到最佳拟合直线。因为计算的是误差平方和，所有，误差正负值之间没有相互抵消。

![这里写图片描述](https://img-blog.csdn.net/20180719205841701?)

![这里写图片描述](https://img-blog.csdn.net/20180719205828718?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

我们可以使用指标 R-square 来评估模型的性能。

**重点：**

* 自变量和因变量之间必须满足线性关系。

* 多元回归存在多重共线性，自相关性和异方差性。

* 线性回归对异常值非常敏感。异常值会严重影响回归线和最终的预测值。

* 多重共线性会增加系数估计的方差，并且使得估计对模型中的微小变化非常敏感。结果是系数估计不稳定。

* 在多个自变量的情况下，我们可以采用正向选择、向后消除和逐步选择的方法来选择最重要的自变量。

### 2) 逻辑回归

逻辑回归用来计算事件成功（Success）或者失败（Failure）的概率。当因变量是二进制（0/1，True/False，Yes/No）时，应该使用逻辑回归。这里，Y 的取值范围为 [0,1]，它可以由下列等式来表示。

```hljs
odds= p/ (1-p) = probability of event occurrence / probability of not event occurrence
ln(odds) = ln(p/(1-p))
logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk
```

* 1
* 2
* 3

其中，p 是事件发生的概率。你可能会有这样的疑问“为什么在等式中使用对数 log 呢？”

因为我们这里使用的二项分布（因变量），所以需要选择一个合适的激活函数能够将输出映射到 [0,1] 之间，Logit 函数满足要求。在上面的等式中，通过使用最大似然估计来得到最佳的参数，而不是使用线性回归最小化平方误差的方法。

![这里写图片描述](https://img-blog.csdn.net/20180719210018331?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**重点：**

* 逻辑回归广泛用于分类问题。

* 逻辑回归不要求因变量和自变量之间是线性关系，它可以处理多类型关系，因为它对预测输出进行了非线性 log 变换。

* 为了避免过拟合和欠拟合，我们应该涵盖所有有用的变量。实际中确保这种情况的一个好的做法是使用逐步筛选的方法来估计逻辑回归。

* 训练样本数量越大越好，因为如果样本数量少，最大似然估计的效果就会比最小二乘法差。

* 自变量不应相互关联，即不存在多重共线性。然而，在分析和建模中，我们可以选择包含分类变量相互作用的影响。

* 如果因变量的值是序数，则称之为序数逻辑回归。

* 如果因变量是多类别的，则称之为多元逻辑回归。

### 3) 多项式回归（Polynomial Regression）

对应一个回归方程，如果自变量的指数大于 1，则它就是多项式回归方程，如下所示：

```hljs
y=a+b*x^2
```

* 1

在多项式回归中，最佳的拟合线不是直线，而是拟合数据点的曲线。

![这里写图片描述](https://img-blog.csdn.net/20180719210145827?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**重点：**

虽然可能会有一些诱导去拟合更高阶的多项式以此来降低误差，但是这样容易发生过拟合。应该画出拟合曲线图形，重点放在确保曲线反映样本真实分布上。下图是一个例子，可以帮助我们理解。

![这里写图片描述](https://img-blog.csdn.net/20180719210216710?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

尤其要注意曲线的两端，看看这些形状和趋势是否有意义。更高的多项式可以产生怪异的推断结果。

### 4) 逐步回归（Stepwise Regression）

当我们处理多个独立变量时，就使用逐步回归。在这种技术中，独立变量的选择是借助于自动过程来完成的，不涉及人工干预。

逐步回归的做法是观察统计值，例如 R-square、t-stats、AIC 指标来辨别重要的变量。基于特定标准，通过增加/删除协变量来逐步拟合回归模型。常见的逐步回归方法如下所示：

* 标准的逐步回归做两件事，每一步中增加或移除自变量。

* 前向选择从模型中最重要的自变量开始，然后每一步中增加变量。

* 反向消除从模型所有的自变量开始，然后每一步中移除最小显著变量。

这种建模技术的目的是通过使用最少的自变量在得到最大的预测能力。它也是处理高维数据集的方法之一。

### 5) 岭回归（Ridge Regression）

岭回归是当数据遭受多重共线性（独立变量高度相关）时使用的一种技术。在多重共线性中，即使最小二乘估计（OLS）是无偏差的，但是方差很大，使得观察智远离真实值。岭回归通过给回归估计中增加额外的偏差度，能够有效减少方差。

之前我们介绍过线性回归方程，如下所示：

<nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" style="width: 6.574em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.26em; height: 0px; font-size: 125%;"><span style="position: absolute; clip: rect(1.717em, 1005.26em, 2.974em, -999.997em); top: -2.569em; left: 0em;"><span class="mrow" id="MathJax-Span-2"><span class="mi" id="MathJax-Span-3" style="font-family: STIXGeneral-Italic;">y</span><span class="mo" id="MathJax-Span-4" style="font-family: STIXGeneral-Regular; padding-left: 0.289em;">=</span><span class="mi" id="MathJax-Span-5" style="font-family: STIXGeneral-Italic; padding-left: 0.289em;">a</span><span class="mo" id="MathJax-Span-6" style="font-family: STIXGeneral-Regular; padding-left: 0.231em;">+</span><span class="mi" id="MathJax-Span-7" style="font-family: STIXGeneral-Italic; padding-left: 0.231em;">b</span><span class="mo" id="MathJax-Span-8" style="font-family: STIXGeneral-Regular; padding-left: 0.231em;">∗</span><span class="mi" id="MathJax-Span-9" style="font-family: STIXGeneral-Italic; padding-left: 0.231em;">x<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.574em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.354em; border-left: 0px solid; width: 0px; height: 1.289em;"></span></span></nobr><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>y</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>∗</mo><mi>x</mi></math>

这个方程也有一个误差项，完整的方程可表示成：

```hljs
y=a+b*x+e (error term),  [error term is the value needed to correct for a prediction error between the observed and predicted value]
=> y=a+y= a+ b1x1+ b2x2+....+e, for multiple independent variables.
```

* 1
* 2

在线性方程中，预测误差可以分解为两个子分量。首先是由于偏颇，其次是由于方差。预测误差可能由于这两个或两个分量中的任何一个而发生。这里，我们将讨论由于方差引起的误差。

岭回归通过收缩参数 λ（lambda）解决了多重共线性问题。请看下面的方程式：

![这里写图片描述](https://img-blog.csdn.net/20180719210419841?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3JlZF9zdG9uZTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

上面这个公式中包含两项。第一个是最小平方项，第二个是系数 β 的平方和项，前面乘以收缩参数 λ。增加第二项的目的是为了缩小系数 β 的幅值以减小方差。

**重点：**

* 除非不假定正态性，岭回归与最小二乘回归的所有假设是一样的。

* 岭回归缩小了系数的值，但没有达到零，这表明它没有特征选择特征。

* 这是一个正则化方法，使用了 L2 正则化。

### 6) 套索回归（Lasso Regression）

类似于岭回归，套索（Least Absolute Shrinkage and Selection Operator）回归惩罚的是回归系数的绝对值。此外，它能够减少变异性和提高线性回归模型的准确性。请看下面的方程式：

![这里写图片描述](https://img-blog.csdn.net/20180719210512316?)

套索回归不同于岭回归，惩罚函数它使用的是系数的绝对值之和，而不是平方。这导致惩罚项（或等价于约束估计的绝对值之和），使得一些回归系数估计恰好为零。施加的惩罚越大，估计就越接近零。实现从 n 个变量中进行选择。

**重点：**

* 除非不假定正态性，套索回归与最小二乘回归的所有假设是一样的。

* 套索回归将系数收缩到零（正好为零），有助于特征选择。

* 这是一个正则化方法，使用了 L1 正则化。

* 如果一组自变量高度相关，那么套索回归只会选择其中一个，而将其余的缩小为零。

### 7) 弹性回归（ElasticNet Regression）

弹性回归是岭回归和套索回归的混合技术，它同时使用 L2 和 L1 正则化。当有多个相关的特征时，弹性网络是有用的。套索回归很可能随机选择其中一个，而弹性回归很可能都会选择。

![这里写图片描述](https://img-blog.csdn.net/2018071921060538?)

权衡岭回归和套索回归的一个优点是它让弹性回归继承了一些岭回归在旋转状态下的稳定性。

**重点：**

* 在高度相关变量的情况下，它支持群体效应。

* 它对所选变量的数目没有限制

* 它具有两个收缩因子 λ1 和 λ2。

除了这 7 种最常用的回归技术之外，你还可以看看其它模型，如 Bayesian、Ecological 和 Robust 回归。

## 4. 如何选择合适的回归模型？

当你只知道一两种技巧时，生活通常是简单的。我知道的一个培训机构告诉他们的学生：如果结果是连续的，使用线性回归；如果结果是二值的，使用逻辑回归！然而，可供选择的选项越多，选择合适的答案就越困难。类似的情况也发生在回归模型选择中。

在多种类型的回归模型中，基于自变量和因变量的类型、数据维数和数据的其它本质特征，选择最合适的技术是很重要的。以下是如何选择合适的回归模型的几点建议：

* 数据挖掘是建立预测模型不可缺少的环节。这应该是选择正确的模型的第一步，比如确定各变量的关系和影响。

* 比较适合于不同模型的拟合程度，我们可以分析它们不同的指标参数，例如统计意义的参数，R-square，Adjusted R-square，AIC，BIC 以及误差项，另一个是 Mallows’ Cp 准则。通过将模型与所有可能的子模型进行对比（或小心地选择他们），检查模型可能的偏差。

* 交叉验证是评价预测模型的最佳方法。你可以将数据集分成两组（训练集和验证集）。通过衡量观测值和预测值之间简单的均方差就能给出预测精度的度量。

* 如果数据集有多个混合变量，则不应使用自动模型选择方法，因为不希望同时将这些混合变量放入模型中。

* 这也取决于你的目标。与高度统计学意义的模型相比，简单的模型更容易实现。

* 回归正则化方法（LasSo、Ridge 和 ElasticNet）在数据集是高维和自变量是多重共线性的情况下工作良好。

**结语：**

现在，我希望你对回归会有一个整体的印象。这些回归技术应该根据不同的数据条件进行选择应用。找出使用哪种回归的最佳方法之一就是检查变量族，即离散变量还是连续变量。

在本文中，我讨论了 7 种类型的回归方法和与每种回归的关键知识点。作为这个行业中的新手，我建议您学习这些技术，并在实际应用中实现这些模型。


## 参考资料
[你应该掌握的 7 种回归模型！](https://blog.csdn.net/red_stone1/article/details/81122926)