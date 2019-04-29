---
layout: post
title: 伯努利试验
category: 数学和算法
keywords: 伯努利试验
---


## 什么是伯努利试验

在概率论中，把在同样条件下重复进行试验的数学模型称为独立试验序列概型,进行n次试验，若任何一次试验中各结果发生的可能性都不受其它次试验结果发生情况的影响，则称这n次试验是相互独立的。特别的，当每次试验只有两个可能结果时，称为n重伯努利试验

典例

* 连续的n次射击；
* 连续的掷n次硬币。


## 相关定理

设在一次试验中，事件A发生的概率为p（0<p<1），则在n重伯努利试验中，事件A恰好发生 k 次的概率为：

![](https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D280/sign=bbef08f33ffae6cd08b4ac693fb10f9e/4bed2e738bd4b31cabc57d7f8dd6277f9f2ff87d.jpg) 。<sup class="sup--normal" data-sup="3" data-ctrmap=":3,">[3]</sup> 


设在一次试验中，事件A首次发生的概率为p(0<p<1)，则在伯努利试验序列中，事件A在第 k 次试验中才首次发生的概率为

![](https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D166/sign=84c74c7baaec08fa220017a16fec3d4d/c8ea15ce36d3d539c5c4e7073087e950342ab07d.jpg) 。



## 二项分布
二项分布就是重复n次独立的伯努利试验。在每次试验中只有两种可能的结果，而且两种结果发生与否互相对立，并且相互独立，与其它各次试验结果无关，事件发生与否的概率在每一次独立试验中都保持不变，则这一系列试验总称为n重伯努利实验，当试验次数为1时，二项分布服从0-1分布。