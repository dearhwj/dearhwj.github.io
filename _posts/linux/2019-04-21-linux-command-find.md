---
keywords: hostname,ifconfig
layout: post
title: Linux find命令
category: find
---

## 正文
### find删除指定时间之前的文件
[原文地址:https://www.cnblogs.com/dplearning/p/6043158.html](https://www.cnblogs.com/dplearning/p/6043158.html)

```
find .  -type f  -name *.log  -mtime +180  -exec rm {} \;
解析：

find 后面紧跟的是要查找的目录，. 表示当前目录

-type f：指定查找对象为文件

-name *.log：指定查找对象名称以.log结尾

-mtime +180: 查找180天以前的老文件

-exec rm {} \;  :执行删除命令，这句长得很奇怪，后面有个 {} \; 是必须的，也可以执行其他指令，比如ls， rm -i之类的

```


下面指令显示查找到文件的详细信息

```
find . -type f -mtime -180 -exec ls -l {} \; | more

```
 后面用管道，实现分页显示

查看2016-11-03日的数据
```
find . -newermt '2016-11-03' ! -newermt '2016-11-04' -exec ls -l {} \;
```


### find命令Tips

[find命令不区分大小写](http://www.linuxdiyf.com/linux/13964.html)

	Linux使用find命令搜索文件时如果不清楚文件的名称中是否包含的大写，你可以使用 -iname参数来忽略大小写.