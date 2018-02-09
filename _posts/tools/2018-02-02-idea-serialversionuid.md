---
layout: post
title: Intellij IDEA 自动生成 serialVersionUID
category: 开发工具
keywords: IntelliJ
--- 


Setting->Inspections->Serialization issues->Serializable class without ’serialVersionUID’ 
选上以后，在你的class中：Alt+Enter就会提示自动创建serialVersionUID了。

![](/images/idea_serialversionuid_setting.jpg)