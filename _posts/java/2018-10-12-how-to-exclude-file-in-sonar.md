---
layout: post
title:  sonar如何排除指定的目录
category: JAVA
keywords: Sonar
---

## 正文

现在系统通常都会有自动化生成的代码，在使用Sonar做系统代码质量分析的时候我们都希望能把自动生成的代码排除到系统分析之外。要实现这个就非常简单了，在maven的pom.xml文件里面加入sonar.exclusions指明哪些自动生成代码的文件夹不需要分析。

具体的匹配规则可以参考sonar的官方文档，非常简单 （docs.sonarqube.org ）。注意使用maven项目时匹配的文件夹基础是project base dir。 
Wildcard Matches 
? 匹配单个字符 
** 匹配0个或多个文件夹

匹配0个或多个字符
例子：

```
<properties>
    <sonar.exclusions>
        src/main/java/com/alibaba/rhino/aps/prodplan/dal/**/*
    </sonar.exclusions>
</properties>

```
