---
layout: post
title: 相识性度量算法
category: 数学和算法
keywords: 欧式距离
---
## 正文
[原文地址](https://blog.csdn.net/weixin_41770169/article/details/80659236)

1. 欧式距离
2. 曼哈顿距离
3. Mahalanobis马氏距离
4. cosine similarity
5. Hammi汉明距离




### 欧氏距离Euclidean Distance：

![](https://img-blog.csdn.net/20180611230549668?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTc3MDE2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 曼哈顿距离[Manhattan](https://www.baidu.com/s?wd=Manhattan&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)：

![](https://img-blog.csdn.net/2018061123072969?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTc3MDE2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20180611230739451?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTc3MDE2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### Mahalanobis马氏距离

马氏距离的浅显解释，见我的博文：https://blog.csdn.net/weixin_41770169/article/details/80759195

马氏距离和欧式距离的对比，见我的博文：https://blog.csdn.net/weixin_41770169/article/details/80759236

![](https://img-blog.csdn.net/20180621135314304?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTc3MDE2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### cosine similarity

![](https://img-blog.csdn.net/20180621135440697?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTc3MDE2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

cosine distance = 1 - cosine similarity

### Hammi汉明距离

汉明距离是一个概念，它表示两个（相同长度）字对应位不同的数量

比如：1011101 与 1001001 之间的汉明距离是 2


### 参考资料
[曼哈顿距离](https://baike.baidu.com/item/%E6%9B%BC%E5%93%88%E9%A1%BF%E8%B7%9D%E7%A6%BB)
[kNN算法综述](https://wenku.baidu.com/view/d84cf670a5e9856a561260ce.html)
