---
layout: post
title: Shell脚本增加主机名IP绑定
category: Shell脚本
keywords: hostname,ifconfig
--- 

## 原文

原文地址:[https://segmentfault.com/q/1010000000735532](https://segmentfault.com/q/1010000000735532)

```
HOSTNAME=`hostname`
ip_addr=`/sbin/ifconfig eth0 |grep -a "inet addr:" |awk -F":" '{print $2}' |egrep -o '([0-9]{1,3}\.?){4}'`
echo ${ip_addr} > temp.txt
sudo sh -c 'echo "`cat temp.txt` ${HOSTNAME}" >> /etc/hosts'

```