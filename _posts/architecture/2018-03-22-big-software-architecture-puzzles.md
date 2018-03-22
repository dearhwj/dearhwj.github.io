---
layout: post
title: 软件体系设计过程中需要面对的难题
category: 软件架构和设计
---

## 正文

1. 复杂性。 该体系结构的复杂性对于域而言是否合理？ 反之，该样式对于域而言是否过于简单？ 在这种情况下，风险是最终只设计出一个泥球，因为该体系结构无助于利落地管理依赖项。

1. 异步消息传送和最终一致性。 异步消息传送可用于分离服务，提高可靠性（因为消息可以重试）和可伸缩性。 但是，这也带来了“永远/一次”语义和最终一致性等方面的难题。

2. 服务间通信。 将应用程序分解为独立的服务时，风险是服务之间的通信会导致不可接受的延迟，或造成网络拥塞（例如，在微服务体系结构中）。

3. 可管理性。 管理应用程序、监视、部署更新以及其他操作的难度有多大？


### 参考
[https://docs.microsoft.com/zh-cn/azure/architecture/guide/architecture-styles/index](https://docs.microsoft.com/zh-cn/azure/architecture/guide/architecture-styles/index)