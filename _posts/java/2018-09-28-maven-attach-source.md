---
layout: post
title:  Maven打包生成源码包和Javadoc包
category: JAVA
keywords: Maven
---

## 正文
原文地址:[https://blog.csdn.net/blue_dd/article/details/53183441](https://blog.csdn.net/blue_dd/article/details/53183441)

```
<build>
	<plugins>
		<plugin>
			<groupId>org.apache.maven.plugins</groupId>
			<artifactId>maven-source-plugin</artifactId>
			<version>2.1.2</version>
			<executions>
				<execution>
					<id>attach-sources</id>
					<phase>verify</phase>
					<goals>
						<goal>jar-no-fork</goal>
					</goals>
				</execution>
			</executions>
		</plugin>
	</plugins>
</build>
```

