---
layout: post
title:  Fastjson操作指南
category: JAVA
keywords: fastjson
---


## 基本用法
###  把java对象序列化为JSON字符串
Fastjson将java对象序列化为JSON字符串，fastjson提供了一个最简单的入口

```
package com.alibaba.fastjson;

public abstract class JSON {
    public static String toJSONString(Object object);
}
```
Fastjson在1.2.11版本中，JSON类新增对OutputStream/Writer直接支持。

```
public abstract class JSON {
   public static final int writeJSONString(OutputStream os, // 
                                             Object object, // 
                                             SerializerFeature... features) throws IOException;

    public static final int writeJSONString(OutputStream os, //
                                             Charset charset, //  
                                             Object object, // 
                                             SerializerFeature... features) throws IOException;

   public static final int writeJSONString(Writer os, // 
                                             Object object, // 
                                             SerializerFeature... features) throws IOException;
}


```

### 把JSON字符串转换成JAVA对象

```
import com.alibaba.fastjson;
import java.nio.charset.Charset;
class Model {
    public int value;
}

InputStream is = ...
Model model = JSON.parseObject(is, Model.class);
Model model2 = JSON.parseObject(is, Charset.from("UTF-8"), Model.class);

```

## 定制Fastjon序列化

fastjson支持多种方式定制序列化

* 通过@JSONField定制序列化
* 通过@JSONType定制序列化
* 通过SerializeFilter定制序列化
* 通过ParseProcess定制反序列化


### 通过@JSONField定制序列化

先看一下JSONField的Annotation，JSONField提供了ordinal、name、serialize若干定制属性

```
public @interface JSONField {
    /**
     * config encode/decode ordinal
     * @since 1.1.42
     * @return
     */
    int ordinal() default 0;

    String name() default "";

    String format() default "";

    boolean serialize() default true;

    boolean deserialize() default true;

    SerializerFeature[] serialzeFeatures() default {};

    Feature[] parseFeatures() default {};
    
    String label() default "";
    
    /**
     * @since 1.2.12
     */
    boolean jsonDirect() default false;
    
    /**
     * Serializer class to use for serializing associated value.
     * 
     * @since 1.2.16
     */
    Class<?> serializeUsing() default Void.class;
    
    /**
     * Deserializer class to use for deserializing associated value. 
     * 
     * @since 1.2.16 
     */
    Class<?> deserializeUsing() default Void.class;

    /**
     * @since 1.2.21
     * @return the alternative names of the field when it is deserialized
     */
    String[] alternateNames() default {};

    /**
     * @since 1.2.31
     */
    boolean unwrapped() default false;
}

```

* 使用ordinal指定字段的顺序
* 使用serialize/deserialize指定字段不序列化
* 使用format配置日期格式化
* 使用serializeUsing制定属性的序列化类
* alternateNames:在fastjson在1.2.21版本中提供了一个借鉴自gson的特性，支持反序列化时使用多个不同的字段名称，使用的方式是配置JSONField的alternateNames。

### SerializeFilter(Fastjson的序列化属性)

```
	QuoteFieldNames 双引号字段名称
	SkipTransientField 忽略TransientField
	UseSingleQuotes  使用单引号
	WriteMapNullValue 是否输出值为null的字段,默认为false
	WriteEnumUsingToString “用枚举toString()值输出”
	WriteEnumUsingName		用枚举name()输出
	UseISO8601DateFormat	“用ISO8601DateFormat日期格式”
	WriteNullListAsEmpty	list是null的时候输出空列表
	WriteNullStringAsEmpty	sting是null的时候，输出空字符串
	WriteNullBooleanAsFalse	 boolean null值，输出false
	SortField	排序SortField
	PrettyFormat	输出格式优化
	WriteClassName	输出ClassName
	DisableCircularReferenceDetect	禁止循环引用
	WriteSlashAsSpecial	
	BrowserSecure
	NotWriteDefaultValue  不输出缺省值
	WriteNonStringKeyAsString	输出
	BeanToArray				bean换成Array
	DisableCheckSpecialChar	禁止特殊字符检查
	NotWriteRootClassName	不输出根class名称
	WriteDateUseDateFormat	
	BrowserCompatible


```



## FastJson参考
[参考文档](https://www.w3cschool.cn/fastjson/)   
[fastjson设置指定日期属性的格式化](https://blog.csdn.net/john1337/article/details/76277617)