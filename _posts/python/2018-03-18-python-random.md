---
keywords: Python
layout: post
title: Python随机数生成
category: Python
---


## 正文
```
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 生成 0 ~ 9 之间的随机数
 
# 导入 random(随机数) 模块
import random
 
print(random.randint(0,9))
```
执行以上代码输出结果为：
```
4
```

以上实例我们使用了 random 模块的 randint() 函数来生成随机数，你每次执行后都返回不同的数字（0 到 9），该函数的语法为：

```
random.randint(a,b)
```

函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。