---
layout: post
title: 离散事件系统和仿真
category: 智能制造
keywords: 离散事件,离散事件系统,仿真
---

##  离散事件系统

### 什么是离散事件系统

人们在生产活动和社会活动中，经常遇到一类复杂的系统，这类系统中有许多事件时而出现，时而消失，时而动作，时而停止，而启动和停止都发生在一些离散的时刻，并带有一定的随机性。例如，港口中船舶的停靠码头、生产线上机床的启停、电话的接通和断开、计算机系统中某项作业的进行和退出，凡此种种，都带有上述特点，这类系统叫做离散事件动态系统(DEDS)。


###  离散事件系统的特点

这类系统的分析研究，需要考虑下面这些特点：
1. 它是由事件驱动发生变化的，带有不连续性。
2. 但考核它的性能的指标却带有连续特点，例如平均吞吐率、等候时间、利用率等。
3. 随机特点。因为有些驱动系统的事件的到来带有随机特点(如顾客的到来、电讯报文的到达)，此外任务的完成、任务间的衔接等也都有一定的随机性，所以常常需要使用处理概率事件与随机过程的方法和技术。
4. 层次性特点。由于这类系统一般是人造复杂系统，所以多半是按层次组织的，例如在空间跨度上，有单机、机组、生产线、车间、工厂几个层次，在时间跨度上，有小时、班(8小时)、日、周、月、年等层次，在组织结构上更是如此。这样我们不得不对每个层次都建立相应的分析方法，有时需要集成，有时又需要分解，上下还必须协调。
5. 动态性特点。我们必须研究这类系统的动态行为和过渡过程。
6. 计算复杂性。在这类系统中，由于组成单元数目大，事件状态多，所以常有“组合爆炸”的危险，这给分析计算带来了很大困难。 [1] 






## 离散事件系统仿真

### 方法简介
用计算机对离散事件系统进行仿真实验的方法。这种仿真实验的步骤包括：画出系统的工作流程图，确定到达模型、服务模型和排队模型（它们构成离散事件系统的仿真模型），编制描述系统活动的运行程序并在计算机上执行这个程序。离散事件系统仿真广泛用于交通管理、生产调度、资源利用、计算机网络系统的分析和设计方面。


### 到达模型
用来描述临时实体（“顾客”）到达的时间特性。若临时实体1到达系统的时刻为t1,临时实体2到达系统的时刻为t2,则两者之间的时间间隔Ta称为临时实体互相到达时间(Ta=t2-t1),并用Ta大于时间t的概率（称为到达分布函数A0(t)）来表示到达模型。假设临时实体何时到达完全是随机的，即第k个临时实体到达的时间与第k-1个临时实体到达的时间无关,而且在时间区间Δt内到达的概率正比于Δt，那么到达分布函数可以表示为A0(t)=e-λt(λ=1/Ta,称为互相到达速度)。这种到达模型称为泊松到达模型，它对研究离散事件系统有很重要的实用价值。

### 服务模型 　
用来描述永久实体（“服务台”）为临时实体服务的时间特性。假设永久实体为单个临时实体服务所需要的时间为TS，则用TS大于时间t的概率（称为服务分布函数s0(t)来表示服务模型。如果服务时间完全是随机的，则S0(t)=e-μt（μ=1/TS称为服务速度）。多数的情况是服务时间在一个常数附近波动。例如一台机床加工一个零件所花费的期望时间是固定的，但是由于每个零件切削用量和材料刚性都是随机变化的，所以加工时间就会发生波动。此时可用正态分布来描述服务模型。

### 排队模型
当永久实体的服务速度μ低于临时实体互相到达速度λ时，在永久实体前面会出现排队现象。此时在一次服务完毕后，系统即按照一定的规则从等候服务的队列中挑选下一个接受服务的临时实体，这种规则就称为排队模型。常用的排队模型有先进先出制、后进先出制和随机服务制等。

### 参考资料

[离散事件系统]([https://baike.baidu.com/item/%E7%A6%BB%E6%95%A3%E4%BA%8B%E4%BB%B6%E5%8A%A8%E6%80%81%E7%B3%BB%E7%BB%9F?fromtitle=%E7%A6%BB%E6%95%A3%E4%BA%8B%E4%BB%B6%E7%B3%BB%E7%BB%9F&fromid=15944228](https://baike.baidu.com/item/离散事件动态系统?fromtitle=离散事件系统&fromid=15944228))

[离散事件系统仿真方法](https://baike.baidu.com/item/%E7%A6%BB%E6%95%A3%E4%BA%8B%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%BB%BF%E7%9C%9F%E6%96%B9%E6%B3%95)