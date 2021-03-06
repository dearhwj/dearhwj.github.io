# 笔记：架构风格与基于网络的软件架构设计
原文：[架构风格与基于网络的软件架构设计](architectural_styles_and_the_design_of_network_based_software_architectures.pdf)
## 软件架构
### 运行时抽象

一个软件架构是一个软件系统在其操作的某个阶段的运行时(run-time)元素的抽象一个系统可能由很多层抽象和很多个操作阶段组成，每个抽象和操作阶段都 有自己的软件架构。

### 组件
1. 一个组件是软件指令和内部状态的一个抽象单元，通过其接口提供对于数据的转换。
2. 每个组件的行为是架构的一部分，能够被其他组件观察到(observed)或看 到(discerned);组件应该由它为其他组件提供的接口和服务来定义，而不是由它在接口之后的实现来定义。

### 连接器
1. 一个连接器是对于组件之间的通讯、协调或者合作进行仲裁的一种抽象机制。
2. 连接器通过将数据元素从它的一 个接口转移(transferring)到另一个接口而不改变数据，来支持组件之间的通信。在其内部， 一个连接器可以包含一个由组件组成的子系统，为了转移的目的对数据进行某种转换、执行 转移、然后做相反的转换并交付与原始数据相同的结果。

### 数据
1. 一个数据是组件通过一个连接器接收或发送的信息元素；但是不包括那些永久驻留或隐藏在组件中的信息。

### 配置
1. 一个配置是在系统的运行期间组件、连接器和数据之间的架构关系的结构。

### 属性
软件架构的架构属性集合包括了对组件、连接器和数据的选择和排列所导致的所有属性。 架构属性的例子包括了可以由系统获得的功能属性和非功能属性，例如:进化的相对容易程 度、组件的可重用性、效率、动态扩展能力;这些常常被称作品质属性(quality attributes )。属性是由架构中的一组约束所导致的。约束往往是由在架构元素的某个方面应用软件工 程原则[58]来驱动的。例如，统一管道和过滤器(uniform pipe-and-filter)风格通过在其组件 接口之上应用通用性(generality)原则——强迫组件实现单一的接口类型，从应用中获得了 组件的可重用性和可配置性的品质。因此，架构约束是由通用性原则所驱动的“统一组件接 口”，目的是获得两个想要得到的品质，当在架构中实现了这种风格时，这两个品质将成为 可重用和可配置组件的架构属性。

### 风格
1. 一种架构风格是一组协作的架构约束，这些约束限制了架构元素的角色和功能，以及在任何一个遵循该风格的架构中允许存在的元素之间的关系。
2. 明确地说，一种架构风格决定了在此风格的实例中能 够使用的组件和连接器的词汇表，以及一组如何能够将它们组合在一起的约束
3. 选择正确的架构风格必须要理解该问题领域

### 视图
三种重要的软件架构视 图:处理、数据、连接。处理视图侧重于流过组件的数据流，以及组件之间连接(the connections among the components)的那些与数据相关的方面。数据视图侧重于处理的流程， 而不是连接器。连接视图侧重于组件之间的关系和通信的状态。


### 设计、设计模式、模式语言手册软件设计模式比架构风格更加倾向于面向特定的问题

## 基于网络的应用的架构
### 基于网络 vs. 分布式分布式系统在用户看来像是普通的集中式系统，但是运行在多个独立的 CPU 之上。相反，基于网络的系统有能力跨越网络运转，但是这一点无需表达为对用户透明的方式。在某些情况下， 还希望用户知道一个需要网络请求的动作和一个在他们的本地系统就能满足的动作之间的差 别，尤其是当使用网络意味着额外的处理成本的时候 

### 应用软件 vs. 网络软件
1. 应用软件代表的是一个系统的“理解业务”(business-aware)的那部分功能
2. 应用软件的架构是对于整个系统的一种抽象，其中用户动作的目的可以被表示为一个架构的功能属性。

### 评估应用软件架构的设计
* 架构是架构设计的实现，而非设计本身


## 关键关注点的架构属性
有时候也被称作软件质量(software qualities)。

1. 性能(Performance)
	2. 网络性能(Network Performance)
	3. 用户可觉察的性能(User-perceived Performance)
	4. 网络效率(Network Efficiency)
2. 可伸缩性(Scalability)
3. 简单性(Simplicity)
4. 可修改性(Modifiability)
5. 可进化性(Evolvability)
	6. 可进化性(Evolvability)
	7. 可扩展性(Extensibility)
	8. 可定制性(Customizability)
	9. 可配置性(Configurability)
	10. 可重用性(Reusability)
6. 可见性(Visibility)
7. 可移植性(Portability)
8. 可靠性(Reliability)

### 性能
应用软件都无法回避为了实现该软件的需 求而付出的基本成本。

网络性能：一种鼓励小型的强类型(strongly typed)交互的风格，对于一个在已知组件之间转移 小型数据的应用来说会很有效率，但是会在包括了大型数据转移或协商接口(negotiated interfaces)的应用中导致过多的负载。同样地，一种通过多个组件之间协调来过滤大型数据 流的风格，在主要需要小型的控制消息的应用中会显得不合时宜。

用户可觉察的性能(User-perceived Performance)：如果算法在产生已编码的转换之前，对数据的重要部分进行采样，则对于一段数 据流的压缩就能够产生更加有效率的编码。对于跨越网络转移已编码的数据来说，这会导致 更短的完成时间。然而，如果压缩是在响应用户动作的过程中以一种即时(on-the-fly)的方 式来执行的，在转移之前缓存大型的采样数据会产生不可接受的延迟。平衡这些权衡是很困 难的，特别是当不知道接收者是更关心延迟(例如，Web 浏览器)还是更关心完成时间(例 如，Web 爬虫)的时候。

网络效率(Network Efficiency)：关于基于网络的应用的一个有趣的观察是:最佳的应用性能是通过不使用网络而获得的。这基本上意味着对于一个基于网络的应用，最高效的架构风格是那些在可能的情况下，能够有效地将对于网络的使用减到最少的架构风格。可以通过重用先前的交互(缓存)、减少与用户动作相关的网络交互(复制数据和关闭连接操作)、或者通过将对数据的处理移到距离数据源更近的地方(移动代码)来减少某些交互的必要性。

可伸缩性(Scalability)：可伸缩性表示在一个主动的配置中，架构支持大量的组件或大量的组件之间交互的能力。

简单性(Simplicity)：通过架构风格来导致简单性属性的主要方法是，对组件之间的功能分配应用分离关注点 原则(principle of separation of concerns)。如果功能分配使得单独的组件足够简单，那么它 们就更容易被理解和实现。同样地，这样的关注点分离也使得关于整体架构的推理任务变得 更加容易。我选择将复杂性(complexity)、可理解性(understandability)和可验证性 (verifiability)统一在简单性这个通用的属性中，是因为它们在基于网络的系统中有着密切 的关联。对架构元素应用通用性原则(principle of generality)也有助于提高简单性，因为它减少 了架构中的变数。

可修改性(Modifiability):可修改性是对于应用的架构所作的修改的容易程度。可修改性能够被进一步分解为在下 面所描述的可进化性、可扩展性、可定制性、可配置性和可重用性。基于网络的系统的一个 特殊的关注点是动态的可修改性[98]，它要求在对一个已部署的应用做修改时，无需停止和 重新启动整个系统。

可进化性(Evolvability):进化性代表了一个组件实现能够被改变而不会对其他组件产生负面影响的程度。组件的 静态进化通常依赖于其实现是否加强了架构的抽象，因此这并非是任何特定架构风格所独有 的。

可扩展性:可扩展性被定义为将功能添加到一个系统中的能力[108]。动态可扩展性意味着功能能 够被添加到一个已部署的系统中，而不会影响到系统的其他部分。导致可扩展性的方法是在 一个架构中减少组件之间的耦合，就像在基于事件的集成(event-based intergration)的例子 中展示的那样。

可定制性(Customizability):可定制性是指临时性地规定一个架构元素的行为的能力，然后该元素能够提供一种非常规的服务。可定制性是通过远程求值(remote evaluation)风格和按需代码(code-on- demand)风格所导致的一种架构属性。

可配置性(Configurability)：可配置性既与可扩展性有关，也与可重用性有关，因为它是指在部署后(post- deployment)对于组件，或者对于组件配置的修改，这样组件能够使用新的服务或者新的数 据元素类型。管道和过滤器风格和按需代码风格是两个可以分别为组件配置和组件带来可配 置性的例子。
可重用性(Reusability)可重用性(Reusability)：可重用性是应用的架构的一个属性，如果一个应用的架构中的组件、连接器或数据元素能够在不做修改的情况下在其他应用中重用，那么该架构就具有可重用性。在架构风格中导致可重用性的主要机制是降低组件之间的耦合(对于其他组件的标识的了解)和强制使用通用的组件接口。统一管道和过滤器风格是这种约束(译者注:即，强制使用通用的组件接口)的例子。可见性(Visibility)：风格也能够通过限制必须使用通用性的接口，或者提供访问监视功能的方法，来影响基 于网络的应用中交互的可见性。在这种情况下，可见性是指一个组件对于其他两个组件之间 的交互进行监视或仲裁的能力。可见性能够通过以下方式改善性能:交互的共享缓存、通过 分层服务提供可伸缩性、通过反射式监视(reflective monitoring)提供可靠性、以及通过允 许中间组件(例如，网络防火墙)对交互做检查提供安全性。移动代理风格(mobile agent style)是缺乏可见性可能会导致安全问题的一个例子。

可移植性(Portability)：如果软件能够在不同的环境下运行，软件就是可移植的[58]。会导致可移植性属性的风 格包括那些将代码和代码所要处理的数据一起移动的风格，例如虚拟机和移动代理(mobile agent)风格;以及那些限制只能使用标准格式的数据元素的风格。

可靠性(Reliability)：从应用的架构角度来说，可靠性可以被看作当在组件、连接器或数据之中出现部分故障时，一个架构容易受到系统层面故障影响的程度。架构风格能够通过以下方法提高可靠性:避免单点故障、增加冗余、允许监视、以及用可恢复的动作来缩小故障的范围。


## 风格所导致的架构属性
减号(-)表示消极影响，加号(+)表示积极影响，加减号(±)表示影响的性质依赖于问题领域的某个方面。### 数据流风格(Data-flow Styles)#### 管道和过滤器风格中(Pipe and Filter，PF)
每个组件(过滤器)从其输入端读取数据流并在其输出端产生 数据流，通常对输入流应用一种转换并增量地处理它们，以使输出在输入被完全处理完之前 就能够开始[53]。这种风格也被称作单路数据流网络(one-way data flow network)[6]。这里 的架构约束是一个过滤器必须完全独立于其他的过滤器(零耦合):它不能与其他过滤器在 其上行和下行数据流接口分享状态、控制线程或标识[53]。


#### 统一管道和过滤器(Uniform Pipe and Filter，UPF)
统一管道和过滤器风格在 PF 风格的基础上，添加了一个约束，即所有过滤器必须具有 相同的接口。这种风格的主要实例出现在 Unix 操作系统中，其中过滤器进程具有由一个字 符输入数据流(stdin)和两个字符输出数据流(stdout 和 stderr)组成的接口。通过限定使用 这个接口，就能够随意排列组合独立开发的过滤器，从而形成新的应用。这也简化了理解一 个特定的过滤器如何工作的任务。 统一接口的一个缺点是:如果数据需要被转换为它的原始格式或者从它的原始格式转换为特定的格式，这个约束可能会降低网络性能。


|架构风格|继承|网络性能|用户可察觉性能|效率|可伸缩性|简单性|可进化性|可扩展性|可定制性|可配置性|可重用性|可见性|可移植性|可靠性|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|管道和过滤器|||+/-|||+|+|+||+|+|||||
|统一管道和过滤器|管道和过滤器|-|+/-|||++|+|+||++|++|+||||


### 复制风格(Replication Styles)
#### 复制仓库(Replicated Repository，RR)
基于复制仓库风格[6]的系统通过利用多个进程提供相同的服务，来改善数据的可访问 性(accessibility of data)和服务的可伸缩性(scalability of service)。这些分散的服务器交 互为客户端制造出只有一个集中的服务的“幻觉”。主要的例子包括诸如 XMS [49]这样的 分布式文件系统和 CVS[www.cyclic.com]这样的远程版本控制系统。RR 风格的主要优点在于改善了用户可觉察的性能，实现途径是通过减少处理正常请求 的延迟，并在主服务器故障或有意的线下漫游(intentional roaming off the network)时支持 离线操作(disconnected operation)。在这里，简单性是不确定的，因为 RR 风格允许不关心 网络(network-unaware)的组件能够透明地操作本地的复制数据，这补偿了复制所导致的复 杂性。维护一致性是 RR 风格的主要关注点。

#### 缓存(Cache)
复制仓库风格的一种变体是缓存风格:复制个别请求的结果，以便可以被后面的请求重 用。这种形式的复制最常出现在潜在的数据集远远超出单个客户端的容量的情况下，例如在 WWW[20]中，或者在不必完全访问仓库的地方。可以执行延迟复制(lazy replication):当 复制一个请求的尚未缓存的响应数据时，根据引用的局部性(locality of reference)和兴趣的 趋同性(commonality of interest)，将有用的数据项复制到缓存中以备稍后重用。还可以执 行执行主动复制(active replication):基于预测到的请求来预先获取可缓存的数据项。：与复制仓库风格相比，缓存风格对于用户可觉察性能的改善较少，因为没有命中缓存的请求会更多，只有近期被访问过的数据才能被离线操作使用。另一方面，缓存风格实现起来 要容易得多，不需要复制仓库风格那么多的处理和存储，而且由于只有当数据被请求时才会 传输数据，因此缓存风格更加高效。缓存风格当与客户-无状态-服务器风格(client- stateless- server style)结合后就成为了一种基于网络的架构风格


|架构风格|继承|网络性能|用户可察觉性能|效率|可伸缩性|简单性|可进化性|可扩展性|可定制性|可配置性|可重用性|可见性|可移植性|可靠性|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|RR|||++||+|||||||||+|
|Cache|RR||+|+|+|+||||||||||

### 分层风格(Hierarchical Styles)


#### 客户-服务器组件
一个客户是一个触发进程;一个服务器是 一个反应进程。客户端发送请求触发服务器的反应。这样，客户端可以在它所选择的时间启 动活动;然后它通常等待直到请求的服务完成处理。另一方面，服务器等待接收请求，并对 请求作出反应。服务器通常是一个永不终止的进程，并且常常为多个客户端提供服务。分离关注点是在客户-服务器约束背后的原则。功能的适当分离会简化服务器组件，从 而提高可伸缩性。这种简化所采用的形式通常是将所有的用户接口(译者注:即用户界面) 功能移到客户端组件中。只要接口不发生改变，这种分离允许两种类型的组件独立地进化。客户-服务器的基本形式并不限制应用状态如何在客户端组件和服务器组件之间划分。 这常常由连接器实现所使用的机制来负责，例如远程过程调用(remote procedure call)[23] 或者面向消息的中间件(message-oriented middleware)[131]。

#### 分层系统(Layered System，LS)和分层-客户-服务器(Layered-Client-Server，LCS)
一个分层系统是按照层次来组织的，每一层为在其之上的层提供服务，并且使用在其之 下的层所提供的服务。尽管分层系统被看作一种“单纯”的风格，但是它在基于网络的 系统中的使用仅限于与客户-服务器风格相结合，形成分层-客户-服务器风格。分层系统通过对相邻的外部层之外的所有层隐藏内部层，减少了跨越多层的耦合，从而 改善了可进化性和可重用性。分层系统的例子包括分层通信协议的处理，例如 TCP/IP和 OSI 协议栈[138]，以及硬件接口库。分层系统的主要缺点是它们增加了处理数据的开销和延 迟，降低了用户可觉察的性能[32]。分层-客户-服务器风格在客户-服务器风格的基础上添加了代理(proxy)组件和网关 (gateway)组件。一个代理组件作为一个或多个客户端组件的共享服务器(a shared server)，它接收请求并进行可能的转换后将其转发给服务器。一个网关组件在客户端或代 理看起来像是一个正常的服务器，但是事实上它将请求进行可能的转换后转发给了它的“内 部层”(inner- layer)服务器。这些额外的中间组件添加了很多个层，用来为系统添加诸如 负载均衡和安全性检查这样的功能。基于分层-客户-服务器风格的架构在信息系统文献[131]中常常被称为两层、三层或者多 层架构。LCS 风格也可以作为在大规模分布式系统中管理标识的一种解决方案，在这样的系统 中，了解所有服务器的完整信息是代价高昂的。相反，服务器被组织为多个层次，这样那些 很少被用到的服务可以由中间组件来处理，而不是直接由每个客户端组件来处理[6]。


#### 客户-无状态-服务器(Client-Stateless-Server，CSS)客户-无状态-服务器风格源自客户-服务器风格，并且添加了额外的约束:在服务器组件 之上不允许有会话状态(session state)。从客户端发到服务器的每个请求必须包含理解请求 所必需的全部信息，不能利用任何保存在服务器上的上下文(context)，会话状态全部保存 在客户端。这些约束改善了可见性、可靠性和可伸缩性 3 个架构属性。可见性的改善是因为监视系 统再也不必为了确定请求的全部性质而查看多个请求的数据。可靠性的改善是因为这些约束 简化了从部分故障中恢复的任务[133]。可伸缩性的改善是因为不必保存多个请求之间的状 态，允许服务器组件迅速释放资源并进一步简化其实现。客户-无状态-服务器风格的缺点是:因为我们不能将状态数据保存在服务器上的共享上 下文中，通过增加在一系列请求中发送的重复数据(每次交互的开销)，可能会降低网络性能。

#### 客户-缓存-无状态-服务器(Client-Cache-Stateless-Server，CCSS)客户-缓存-无状态-服务器风格来源于客户-无状态-服务器风格和缓存风格(通过添加缓 存组件)。一个缓存在客户端和服务器之间扮演一个仲裁者:早先请求的响应能够(如果它 们被认为是可缓存的)被重用，以响应稍后的相同请求，如果将该请求转发到服务器，得到 的响应可能与缓存中已有的响应相同。有效地利用此风格的实例系统是 Sun 微系统公司的 NFS[115]。添加缓存组件的好处是，它们有可能部分或全部消除一些交互，从而提高效率和用户可觉察的性能。


#### 分层-客户-缓存-无状态-服务器(Layered-Client-Cache-Stateless-Server，LCCSS)
分层-客户-缓存-无状态-服务器风格通过添加代理和/或网关组件，继承了分层-客户-服 务器风格和客户-缓存-无状态-服务器风格。使用此风格的范例系统是 Internet 域名系统 (DNS)。LCCSS 风格的优点和缺点是 LCS 风格和 CCSS 风格的优点和缺点集合。然而，请注意我 们不能将 CS 风格的贡献计算两次，因为如果贡献来自相同的祖先的话，那么其优点是不可 叠加的


#### 远程会话(Remote Session，RS)远程会话风格是客户-服务器风格的一种变体，它试图使客户端组件(而非服务器组件) 的复杂性最小化或者使得它们的可重用性最大化。每个客户端在服务器上启动一个会话，然 后调用服务器的一系列服务，最后退出会话。应用状态被完全保存在服务器上。这种风格通 常在以下场合中使用:想要使用一个通用的客户端(generic client)(例如 TELNET[106]) 或者通过一个模仿通用客户端的接口(例如 FTP [107])来访问远程服务。远程会话风格的优点是:集中维护在服务器的接口更加容易;当对功能进行扩展时，减少了已部署的客户端中的不一致问题;如果交互利用了服务器上扩展的会话上下文，它能够提高效率。它的缺点是:由于要在服务器上保存应用状态，降低了服务器的可伸缩性;因为监视程序必须要知道服务器的完整状态，降低了交互的可见性


#### 远程数据访问(Remote Data Access，RDA)远程数据访问风格[131]是客户-服务器风格的一种变体，它将应用状态分布在客户端和服务器上。客户端以一种标准的格式发送一个数据库查询(例如 SQL)请求到服务器，服务 器分配一个工作空间并执行这个查询，这可能会导致一个巨大的结果集。客户端能够在结果 集上进行进一步操作(例如表连接)或者每次获取结果的一部分。客户端必须了解服务的数 据结构，以便建造依赖于该结构的查询。远程数据访问风格的优点是:一个巨大的数据集能够在服务器端通过多次迭代的方式逐 渐减少，而不需要通过网络传输完整的数据集，从而改善了效率;通过使用一种标准的查询 语言，从而改善了可见性。这种风格的缺点是:客户端必须像服务器实现那样理解相同的数 据库操作概念(因此缺少简单性);而且在服务器上保存应用的上下文，降低了可伸缩性。 由于部分故障会导致工作空间处于未知状态 ，可靠性也蒙受了损失。尽管能够使用事务机 制(例如，二次提交)来修正可靠性的问题，但是代价是增加了复杂性和交互的开销。

|架构风格|继承|网络性能|用户可察觉性能|效率|可伸缩性|简单性|可进化性|可扩展性|可定制性|可配置性|可重用性|可见性|可移植性|可靠性|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|客户-服务器组件|||||+|+|+|||||||||+|
|分层系统|||-||+||+||||+||+||||
|分层-客户-服务器|客户-服务器组件+分层系统|||-|++|+|++||||+||+||
|客户-无状态-服务器|客户-服务器组件|-|||++|+|+|||||+||+|
|客户-缓存-无状态-服务器|客户-无状态-服务器+Cache|-|+|+|++|+|+|||||+||+|
|分层-客户-缓存-无状态-服务器|分层-客户-服务器+客户-缓存-无状态-服务器|-|+|+|+++|++|++||||+|+|+|+|
|远程会话|客户-服务器组件|||+|-|+|+|||||-|||||
|远程数据访问|客户-服务器组件|||+|-|-||||||+||-|||


### 移动代码风格


#### 虚拟机(Virtual Machine，VM)所有移动代码风格的基础是虚拟机(或解释器)风格[53]。代码必须以某种方式来执行， 首选的方式是在一个满足了安全性和可靠性关注点的受控环境中执行，而这正是虚拟机风格 所提供的。虚拟机风格本身并不是基于网络的风格，但是它通常在客户-服务器风格(REV和 COD 风格)中与一个组件结合在一起使用。虚拟机通常被用作脚本语言的引擎，包括像 Perl[134]这样的通用语言和像 PostScript[2] 这样的与特定任务相关的语言。虚拟机带来的主要好处是在一个特定平台上分离了指令 (instruction)和实现(implementation)(可移植性)，并且使可扩展性变得容易。因为难 以简单地通过查看代码来了解可执行代码将要做什么事情，因此降低了可见性。同时由于需 要对求值环境(evaluation environment)进行管理，也降低了简单性，但在一些情况下可以 通过简化静态的功能(static functionality)得到补偿。


### 远程求值(Remote Evaluation，REV)远程求值风格[50]来源于客户-服务器风格和虚拟机风格，一个客户端组件必须要知道如 何来执行一个服务，但缺少执行此服务所必需的资源(CPU 周期、数据源等等)，这些资源 恰好位于一个远程站点上。因此，客户端将如何执行服务的代码发送给远程站点上的一个服 务器组件，服务器组件使用可用的资源来执行代码，然后将执行结果发送回客户端。这种远 程求值风格假设将要被执行的代码是处在一种受保护的环境中，这样除了那些正在被使用的 资源外，它不会影响到相同服务器的其他客户端。  远程求值风格的优点包括:能够定制服务器组件的服务，这改善了可扩展性和可定制性;当代码能够使它的动作适应于服务器内部的环境(而不是客户端做出一系列交互来做同样的事情)时，能够得到更好的效率(译者注:即通过一次交互，直接发送一段代码到服务器上执行，并且将结果返回);由于需要管理求值的环境，降低了简单性，但在一些情况下可以通过简化静态的服务器功能得到补偿。可伸缩性降低了，但是可以通过服务器对执行环境的管理(杀掉长期运行的代码，或当资源紧张时杀掉大量消耗资源的代码)加以改善，但是管理功能本身会导致与部分故障和可靠性相关的难题。然而，最大的限制是，由于客户端发送代码而不是标准化的查询，因此缺乏可见性。如果服务器无法信任客户端，缺乏可见性会导致明显的部署问题。
  
  
### 按需代码(Code on Demand，COD)在按需代码风格[50]中，一个客户端组件知道如何访问一组资源，但不知道如何处理它 们。它向一个远程服务器发送对于如何处理资源的代码的请求，接收这些代码，然后在本地 执行这些代码。  按需代码风格的优点包括:能够为一个已部署的客户端添加功能，改善了可扩展性和可配置性;当代码能够使它的动作适应于客户端的环境，并在本地与用户交互而不是通过远程交互时，能够得到更好的用户可觉察性能和效率。由于需要管理求值环境，降低了简单性，但在一些情况下可以通过简化静态的客户端功能得到补偿。由于服务器将工作交给了客户端(否则将消耗服务器的资源)，从而改善了服务器的可伸缩性。像远程求值风格一样，最大的限制是由于服务器发送代码而不是简单的数据，因此缺乏可见性。如果客户端无法信任服务器，缺乏可见性会导致明显的部署问题。#### 分层-按需代码-客户-缓存-无状态-服务器(Layered-Code-on-Demand- Client-Cache-Stateless-Server，LCODC$SS)作为一些架构如何互补的例子，考虑将按需代码风格添加到上面讨论过的分层-客户-缓存-无状态-服务器风格上。因为代码被看作不过是另一种数据元素，因此这并不会妨碍 LCCSS 风格的优点。该风格的一个例子是 HotJava Web 浏览器[java.sun.com]，它允许 applet 和协议扩展作为有类型的媒体(typed media)来下载。

#### 移动代理(Mobile Agent，MA)在移动代理风格[50]中，一个完整的计算组件，与它的状态、必需的代码、执行任务所 需的数据一起被移动到远程站点。该风格可以看作来源于远程求值风格和按需代码风格，因 为移动性是同时以这两种方式工作的。移动代理风格超越那些已经在 REV 风格和 COD 风格中描述过的优点的主要优点是:对 于选择在何时移动代码而言，具有更大的灵活性(dynamism)。当一个应用根据推算决定 移动到另一个地点，以减少在该应用和它希望处理的下一组数据之间的距离，此时它可以在 一个地点正处于处理信息的中途(译者注:即不必等待信息完全处理完)。此外，因为应用 状态每次都是在单一地点，所以减少了由局部故障引起的可靠性问题。



|架构风格|继承|网络性能|用户可察觉性能|效率|可伸缩性|简单性|可进化性|可扩展性|可定制性|可配置性|可重用性|可见性|可移植性|可靠性|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|虚拟机||||||+/-||+||||-|+|
|远程求值||||+|-|+/-||+|+|||-|+|-|
|按需代码|||+|+|+|+/-||+||+||-|||
|分层-按需代码-客户-缓存-无状态-服务器||-|++|++|+4+|+++/-|++|+||+|+|+/-|+|+|
|移动代理|||+|++||+/-||++|+|+||-|+||


### 点对点风格(Peer-to-Peer Styles)

#### 基于事件的集成(Event-based Integration，EBI)基于事件的集成风格也被称作隐式调用(implicit invocation)风格或者事件系统(event system)风格，它通过除去了解连接器接口的标识(identity on the connector interface)的必 要性，降低了组件之间的耦合。此风格不是直接调用另一个组件，而是一个组件能够发布 (或广播)一个或者多个事件。在事件发布后，系统中的其他组件能够注册对于某些事件类 型的兴趣，由系统本身来调用所有已注册的组件


#### C2C2 架构风格[128]直接支持大粒度的重用，并且通过加强底层独立性(substrate independence)，支持系统组件的灵活组合。它通过将基于事件的集成风格和分层-客户-服 务器风格相结合来达到这些目标。异步通知消息向下传送，异步请求消息向上传送，这是组 件之间通信的唯一方式。这加强了对高层依赖的松散耦合(服务请求可以被忽略)，并且与 底层实现了零耦合(不知道使用了通知)，从而改善了对于整个系统的控制，又没有丧失 EBI 的大多数优点。


#### 分布式对象(Distributed Objects，DO)分布式对象风格将系统组织为结对进行交互的组件的集合。一个对象是一个实体，这个 实体封装了一些私有的状态信息或数据、操作数据的一组相关的操作或过程、以及一个可能 存在的控制线程，这种封装使得它们能够被整体地看作单个的单元[31]。通常，一个对象的 状态对于所有其他对象而言，是完全隐藏和受到保护的。检查或修改对象状态的唯一方法是 对该对象的一个公共的、可访问的操作发起请求或调用。这样就为每个对象创建了一个良好 定义的接口，在对象的操作实现和它的状态信息保持私有的同时，公开操作对象的规格，这 样做改善了可进化性。


#### 被代理的分布式对象(Brokered Distributed Objects，BDO)为了降低对象标识的影响，现代分布式对象系统通常使用一种或更多种中间风格 (intermediary styles)来辅助通信。这包括基于事件的集成风格和被代理的客户/服务器 (brokered client/server)风格[28]。被代理的分布式对象风格引入了名称解析组件——其目 的是将该组件接收到的客户端请求中一个通用的服务名称解析为一个能够满足该请求的对象 的特定名称，并使用这个特定名称来答复客户端。尽管它改善了可重用性和可进化性，但额 外的间接层要求额外的网络交互，这降低了效率和用户可觉察的性能。被代理的分布式对象系统目前受到两个标准的控制:OMG[97]所开发的 CORBA 行业标 准和 ISO/IEC [66]所开发的开放分布式处理(ODP)的国际标准。  尽管分布式对象引起了非常多的兴趣，然而与大多数其他的基于网络的架构风格相比，这样一类架构风格能够提供的优点很少，它们最适合被使用在包括了对已封装服务(例如硬件设备)的远程调用的应用中，在这些应用中，效率和网络交互的频率并不是很值得关注。
  
  
  |架构风格|继承|网络性能|用户可察觉性能|效率|可伸缩性|简单性|可进化性|可扩展性|可定制性|可配置性|可重用性|可见性|可移植性|可靠性|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|基于事件的集成|||||+|--|+/-|+|+||+|+|-||-|
|C2||||-|+||+|++|+||+|++|+/-|+|+/-|
|分布式对象|||-||+|||+|+||+|+|-||-|
|被代理的分布式对象|||-|-||||++|+||+|++|-|+||


## 设计 Web 架构
Web 的主要目的是旨在成为一种共享的信息空间(a shared information space)，人们和机器都可以通过它来进行沟通。”我们需要的是一种人们用来 保存和构造他们自己的信息的方式，无论信息在性质上是永久的还是短暂的，这样信息对于 他们自己和其他人都是可用的，并且能够引用和构造由其他人保存的信息，而不必每个人都 保持和维护一份本地的副本。

建造一个这样的系统所面对的挑战 是:为这些结构化的信息提供统一的、一致的接口;这些信息可以在尽可能多的平台上获得; 当新的人和新的组织加入到这个项目(译者注:即 Web)时可进行增量的部署。


### 统一接口使 REST 架构风格区别于其他基于网络的架构风格的核心特征是，它强调组件之间要有 一个统一的接口(图 5-6)。通过在组件接口上应用通用性的软件工程原则，整体的系统架 构得到了简化，交互的可见性也得到了改善。实现与它们所提供的服务是解耦的，这促进了 独立的可进化性。然而，付出的代价是，统一接口降低了效率，因为信息都使用标准化的形 式来转移，而不能使用特定于应用的需求的形式。REST 接口被设计为可以高效地转移大粒 度的超媒体数据，并针对 Web 的常见情况做了优化，但是这也导致了该接口对于其他形式 的架构交互并不是最优的