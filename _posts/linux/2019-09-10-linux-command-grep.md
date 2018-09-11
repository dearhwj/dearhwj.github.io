---
keywords: grep
layout: post
title: Linux命令-Grep
category: Linux
---

## 正文

### Tips
####[Linux下grep显示前后几行信息](https://www.cnblogs.com/mfryf/p/3336288.html)

```
grep -C 5 foo file 显示file文件里匹配foo字串那行以及上下5行
grep -B 5 foo file 显示foo及前5行
grep -A 5 foo file 显示foo及后5行
```

#### Linux下grep显示行号

```
grep -n	...
```