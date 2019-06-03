---
layout: post
title: EXCEL CORREL 函数
category: 工具和效率
--- 
## 正文
[原文地址:https://support.office.com/zh-cn/article/correl-%E5%87%BD%E6%95%B0-995dcef7-0c0a-4bed-a3fb-239d7b68ca92](https://support.office.com/zh-cn/article/correl-%E5%87%BD%E6%95%B0-995dcef7-0c0a-4bed-a3fb-239d7b68ca92)



### 语法

CORREL(array1,array2)

CORREL 函数语法具有下列参数：

* **Array1**    必需。值的单元格区域。

* **Array2**    必需。值的第二个单元格区域。




### 备注

* 如果数组或引用参数包含文本、逻辑值或空白单元格，则这些值将被忽略；但包含零值的单元格将计算在内。

* 如果 Array1 和 Array2 的数据点的数量不同，函数 CORREL 返回错误值 #N/A。

* 如果 Array1 或 Array2 为空，或者其数值的 s（标准偏差）等于零，函数 CORREL 返回 #DIV/0! 错误值。

* 相关系数的计算公式为：

![公式](https://support.content.office.net/zh-cn/media/20801406-bfa6-4991-b08f-ebdc0c76af8c.gif)

其中

![X 和 Y](https://support.content.office.net/zh-cn/media/e50bfa35-f7a7-44ee-91eb-d25d79f90f42.png)

是样本平均值 AVERAGE(array1) 和 AVERAGE(array2)。

