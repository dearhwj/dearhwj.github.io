---
layout: post
title:  数据挖掘中的相异度矩阵
category: 数学和算法
keywords: 
typora-root-url: ../../../blog
---

## 相异度矩阵
### 相异度矩阵（Dissimilarity Matrix）
相异度矩阵存储n个对象两两之间的相似性，表现形式是一个n×n维的矩阵。d（i,j）是对象i和j之间相异性的量化表示，通常为非负值，两个对象越相似或“接近”，其值越接近0，越不同，其值越大，且d（i,j）= d（j,i），d（i,i）=0。


### 相异度
相异度d（i,j）的具体计算因所使用的数据类型不同而不同，常用的数据类型包括：
* 区间标度变量
* 二元变量
* 标称型、序数型和比例标度型变量
* 混合类型的变量

### 相异度矩阵是对象—对象结构的一种数据表达方式
多数聚类算法都是建立在相异度矩阵基础上，如果数据是以数据矩阵形式给出的，就要将数据矩阵转化为相异度矩阵。对象间的相似度或相异度是基于两个对象间的距离来计算的

## 具体案例分析
![dissimilarity-matrix-example-1](/images/dissimilarity-matrix-example-1.png)

![dissimilarity-matrix-example-2](/images/dissimilarity-matrix-example-2.png)

![dissimilarity-matrix-example-3](/images/dissimilarity-matrix-example-3.png)

![dissimilarity-matrix-example-4](/images/dissimilarity-matrix-example-4.png)

![dissimilarity-matrix-example-5](/images/dissimilarity-matrix-example-5.png)

![dissimilarity-matrix-example-5](/images/dissimilarity-matrix-example-5.png)

![dissimilarity-matrix-example-6](/images/dissimilarity-matrix-example-6.png)