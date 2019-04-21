---
layout: post
title: Mybatis Tips
category: JAVA
keywords: Mybatis
---

## 正文
### Mybatis，Order By排序问题
[原文地址:https://blog.csdn.net/hu_zhiting/article/details/53026448](https://blog.csdn.net/hu_zhiting/article/details/53026448)

用mybatis自动生成工具，会生成几个文件，其中包括~Mapper.XML和~Example文件。我们能够实现基本的增删改查，也是建立在这几个文件的基础上。XML 文件中SelectByExample中有排序的语句


```
 <if test="orderByClause != null">
      order by ${orderByClause}
    </if>
    
```

所以说，在我们逻辑层代码中，利用Example进行条件查询的时候，也可以将orderBy条件写

```
 example.createCriteria().andDeletedEqualTo(false)
            .andTenantIdEqualTo(tenantId)
            .andEntityIdEqualTo(entityId)
            .andEntityTypeEqualTo(entityType);
        example.setOrderByClause(" version desc ");
        return planEntityMapperExt.selectByExample(example).stream().findFirst().orElse(null);
 ```       