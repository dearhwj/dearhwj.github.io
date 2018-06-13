---
layout: post
title: Azure 应用程序的设计原则
category: 软件架构和设计
keywords: 应用架构设计
---

## 正文
原文地址:[https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/index](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/index)

遵循这些设计原则可以提高应用程序的可伸缩性、复原能力和易管理性。

**[自我修复设计](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/self-healing)**。 在分布式系统中，故障时有发生。 设计应用程序以在故障发生时进行自我修复。

**[实现全面冗余](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/redundancy)**。 在应用程序中构建冗余，以避免出现单一故障点。

**[尽量减少协调](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/minimize-coordination)**。 最大程度地减少应用程序服务之间的协调以实现可伸缩性。

**[横向扩展设计](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/scale-out)**。合理设计应用程序，以便能够通过按需添加或删除新实例对应用程序进行横向缩放。

**[通过分区解决限制](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/partition)**。 使用分区来解决数据库、网络和计算限制。

**[运营设计](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/design-for-operations)**。 合理设计应用程序，使运营团队获得所需的工具。

**[使用托管服务](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/managed-services)**。 尽量使用平台即服务 (PaaS) 而不是基础结构即服务 (IaaS)。

**[使用最佳的数据存储完成作业](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/use-the-best-data-store)**。 选择最适合数据的存储技术，并了解如何使用该技术。

**[演变设计](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/design-for-evolution)**。 所有成功的应用程序会不断变化。 演变设计是持续创新的关键。

**[根据业务需求构建](https://docs.microsoft.com/zh-cn/azure/architecture/guide/design-principles/build-for-business)**。 每个设计决策必须与业务要求相称。