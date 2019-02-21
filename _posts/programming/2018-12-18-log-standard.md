---
layout: post
title: 日志使用规范
category: 开发和测试
keywords: 
---

## 如何正确使用日志级别
* info 用于打印程序应该出现的正常状态信息， 便于追踪定位；
* warn 表明系统出现轻微的不合理但不影响运行和使用；
* error 表明出现了系统错误和异常，无法正常完成目标操作。



## 日志格式
总结起来， 错误日志格式可以为：log.error(“[接口名或操作名] [Some Error Msg] happens. [params] [Probably Because]. [Probably need to do].”);log.error(String.format(“[接口名或操作名] [Some Error Msg] happens. [%s]. [Probably Because]. [Probably need to do].”, params));或log.error(“[Some Error Msg] happens to 错误参数或内容 when [in some condition]. [Probably Because]. [Probably need to do].”);log.error(String.format(“[Some Error Msg] happens to %s when [in some condition]. [Probably Because]. [Probably need to do].”, parameters));[Probably Reason]. [Probably need to do]. 在某些情况下可以省略； 在一些重要接口和场景下最好能说明一下。每一条错误日志都是独立的，尽可能完整、具体、直接说明何种场景下发生了什么错误，由什么原因导致，要采用什么措施或步骤。5.意义错误日志是排查问题的重要手段之一。 当我们编程实现一项功能时， 通常会考虑可能发生的各种错误及相应原因：要排查出相应的原因， 就需要一些关键描述来定位原因。这就会形成三元组：错误现象 -> 错误关键描述 -> 最终的错误原因。需要针对每一种错误尽可能提供相应的错误关键描述，从而定位到相应的错误原因。也就是说，编程的时候，要仔细思考， 哪些描述是非常有利于定位错误原因的， 尽可能将这些描述添加到错误日志中。

原文链接:[https://www.jianshu.com/p/0427329bef5b](https://www.jianshu.com/p/0427329bef5b)