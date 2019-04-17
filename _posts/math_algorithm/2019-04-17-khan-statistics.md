---
layout: post
title: 可汗学院统计学学习笔记
category: 数学和算法
keywords: 统计学
---
## 正文


# 第一集：均值 中位数 众数

均值：平均数，算数平均数  
均值计算：所有数字相加之和除以数字的个数  
均值的意义：衡量集中趋势的方法  
中位数：中间的数  
中位数计算：奇数个数据为中间值，偶数个则中间两个值的均值  
中位数意义：衡量集中趋势的另一种方法，是一个数字描述中间的一种方式。  
众数：数据集中出现频率最多的数字

# 第二集：极差 中程数

极差：指的是数据集中数字分开的有多远  
极差计算：数据集中最大的数 - 数据集中最小的数  
极差意义：极差数值越小，数字之间就越紧密  
中程数：最大数和最小数的平均值(算术平均值)  
中程数意义：衡量数据的集中趋势

# 第三集：象形统计图

象形统计图是用象形图像表示数据的一种方式  

![](https://upload-images.jianshu.io/upload_images/11561542-b3d94c3fa939cc5c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/258/format/webp)

示例图片

# 第四集：条形图

![](https://upload-images.jianshu.io/upload_images/11561542-2c6bbae72e2542d6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/473/format/webp)

示例图片

# 第五集：线形图

线形图可以用于随时间变化的事物  

![](https://upload-images.jianshu.io/upload_images/11561542-edd74a4e9bb11d52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/460/format/webp)

示例图片

# 第六集：饼图

![](https://upload-images.jianshu.io/upload_images/11561542-37d1debd33aa90ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/337/format/webp)

示例图片

# 第七集：误导人的线形图

两张线形图对比时纵坐标或横坐标的刻度设置应该以统一标准进行，不然容易产生误导。  

![](https://upload-images.jianshu.io/upload_images/11561542-dc7fac4c756b5e59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/774/format/webp)

示例图片

# 第八集：茎叶图

叶表示最右边的位/各位，茎代表其它位，如十位，下图很好表现了球员得分在分布中的位置以及整体数据的分布状况  

![](https://upload-images.jianshu.io/upload_images/11561542-224d73e0b1511ca3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/644/format/webp)

示例图片

# 第九集：箱线图

箱线图/盒须图是为了体现中位数和散布情况  
核须图会展现数据非散布情况，按照四分位进行划分，它能显示出数据的中位数在哪  
首先需要对数据集中数据进行排序，找出数据集的中位数M  
其次需要找到小于中位数各数的中位数M1（**下四分位数**）以及大于中位数各数的中位数M2（**上四分位数**），此时相当于将数据集划分为四个子集，盒须图是这个划分的图像表示  
作盒须图大的第一件事就是显示所有数据的范围  

![](https://upload-images.jianshu.io/upload_images/11561542-fe91db0fe80e02ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/682/format/webp)

示例图片

# 第十集：箱线图2

![](https://upload-images.jianshu.io/upload_images/11561542-7161d3c6fff21f5e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/856/format/webp)

示例图片  

第一四分区间/1Q…………

# 第十一集 统计：集中趋势

统计学分类 Statistics  
**描述统计学**  descriptive statistics 假设有一个数据集，在不告诉别人所有数据的情况下介绍这些数据的情况，通过一些指示性数字来代表所有的数据，而无需将所有的数据都说一次。  
**推论统计学** inferential statics 运用数据来对事物做结论，假设从总体中得到了一些样本，只需对样本进行一些数学计算，便有可能推断出整体的总体情况  
下面先从描述统计学入手：  
如果提供一组数据需要我们对其进行描述，我们可能需要找到其中最能代表这组数据的个别数字，或者是一些能体现集中趋势的数字  
广义的平均数：描述集中趋势的某特定数值 Average/最能代表一组数据的某个值  ，不是均值 / mean  
这个广义的平均数可以是均值、中位数或众数  
因为离群值的干扰，有时候众数或中位数比均值更能反应数据的集中趋势/描述这组数字

# 第十二集 统计：样本和总体

希腊字母μ代表总体均值 X上加一横表示样本均值

# 第十三集 统计：总体方差

方差记作 δ^2，即δ的平方  
方差是为了更好的理解数据结构，在不放出全部数据的情况下描述数据总体  
总体方差计算公式：(∑(x(i) - μ)^2) / N  
直观来说，方差和标准差都可以用来衡量数据集中的数据点距离均值的远近程度

# 第十四集 统计：样本方差

Sn^2 为样本方差记号，下标n表示样本数为n个  
Sn^2 = ∑(x(i) - 样本均值)^2/ n  
上述的样本方差通常会低估总体方差，更好的总体估计方差（无偏方差）计算如下：  
S(n-1)^2 = ∑(x(i) - 样本均值) ^2/ (n-1)

# 第十五集 统计：标准差

标准差在方差的基础上来看很简单，就是方差的平方根，总体标准差记作δ，样本的标准差记作S  
为什么使用标准差  
1.标准差的单位更好，比如数据单位为cm，则方差计算结果单位为cm^2，而标准差计算结果单位为cm  
2.假设事物分布是钟型曲线，这可以帮助求得事物落在均值一两个标准差范围内的概率

# 第十六集 统计：诸方差公式

求总体方差公式可以化简为：总体所有数的平方求均值，然后减去总体均值的平方


### 参考资料
[原文地址:https://www.jianshu.com/p/b509477fba1c](https://www.jianshu.com/p/b509477fba1c)
