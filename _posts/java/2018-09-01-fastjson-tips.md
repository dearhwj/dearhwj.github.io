---
layout: post
title:  Fastjson Tips
category: JAVA
keywords: fastjson
---

## fastjson设置指定日期属性的格式化
原文地址:[https://blog.csdn.net/john1337/article/details/76277617](https://blog.csdn.net/john1337/article/details/76277617)

```
1.JSONObject.DEFFAULT_DATE_FORMAT="yyyy-MM-dd";//设置日期格式

2.JSONObject.toJSONString(resultMap, SerializerFeature.WriteMapNullValue,SerializerFeature.DisableCircularReferenceDetect,

SerializerFeature.WriteDateUseDateFormat);

但是上面的解决方案面临一个问题，如果不满足上面的条件（多个date属性，而且需要按照不定的格式序列化这些日期属性），那么我们就需要另辟蹊径，使用fastjson的特性来完成：
@JSONField(format="yyyyMMdd")
    private Date date;
@JSONField(format="yyyy-MM-dd HH:mm:ss")
    private Date date1;
    
```    