---
keywords: Crontab
layout: post
title: Crontab 配置和使用
category: Linux

--- 

## Crontab的格式说明
![](images/crontab_format.jpg)


## 查看Crontab日志的方法 

当crontab命令未如预期计划执行的时候，linux下可以通过查看crontab日志回查任务hang住的具体原因，具体查看方法是查看文件/var/log/cron。


## 问题汇总 

1. 问题描述： 写了一个脚本添加至crontab定时任务执行，测试的时候，使用手工运行shell命令执行成功，但是crontab定时任务却并没有执行； 
解决方案： 
这种问题是由于crontab执行是分用户执行的，环境变量的导入会有问题，一般都需要对脚本的路径及输出日志的路径写成绝对路径，同时，在shell脚本中，增加配置文件source ~/.bash_profile，导入环境变量。

2. 问题描述： 
crontab 执行脚本需要将shell脚本的输出重定向至日志文件，日志文件的命名方式为日期.log，如20150101.log。 
可以将crontab任务编写如下：

	test.sh>>./`date -d last-day +%Y%m%d`.log >&1

	



