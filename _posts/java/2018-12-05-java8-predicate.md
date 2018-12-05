---
layout: post
title: JAVA8-Predicate函数使用
category: JAVA
keywords: JAVA8
---
## 主要说明


Predicate<T> 接受一个输入参数，返回一个布尔值结果。该接口包含多种默认方法来将Predicate组合成其他复杂的逻辑（比如：与，或，非）。可以用于接口请求参数校验、判断新老数据是否有变化需要进行更新操作。add--与、or--或、negate--非


## 常用方法

```
1.判断 boolean test(T t);
```


通用的请求参数校验、判断数据是否变更

```
    public class CommonUtils {
    //参数校验
    public static <T> void checkParams(T t, Map<String, Predicate<T>> map) {
        if (isNotEmpty(map)) {
            map.entrySet().forEach(r -> {
                if (r.getValue().test(t))
                    throw new PandaException(PandaCodes.BAD_PARAM, r.getKey());
            });
        }
    }
    //数据变更校验
    public static <T> boolean checkDataIsChange(T t, List<Predicate<T>> list) {
        if (isNotEmpty(list)) {
            return list.stream().anyMatch(r -> r.test(t));
        }
        return false;
    }
}
```

参数校验

```
private Map<String,Predicate<SkuPlatPriceVo>> getCheckParamRules() {
    Map<String, Predicate<SkuPlatPriceVo>> map = new HashMap<>();
        map.put("平台现价需要为0-无穷大", r -> r.getPlatePrice() < 0);
        map.put("平台的platform不能为空", r -> ParamChecker.isBlank(r.getPlatform()));
    return map
}

校验页面传入的skuPlatPriceVo参数：CommonUtils.checkParams(skuPlatPriceVo,getCheckParamRules());
```


数据变更校验

```
private List<Predicate<SkuPlatPriceVo>> getCheckDataIsChangeRules(PcCustomPriceDTO oldData) {
        List<Predicate<SkuPlatPriceVo>> list = new ArrayList<>();
        list.add(r -> oldData.getPrice() != null && r.getPlatePrice() != oldData.getPrice());
        list.add(r -> oldData.getRebate() != null && r.getRebate() != oldData.getRebate());
        return list;
}

校验页面传入的更新操作skuPlatPriceVo数据是否需要发生变更要执行数据库update操作
if(CommonUtils.checkDataIsChange(skuPlatPriceVo,getCheckDataIsChangeRules(dto))){
    数据库数据更新
}
```




## 参考
原文地址:[https://blog.csdn.net/zhouquan_csdn/article/details/74932682](https://blog.csdn.net/zhouquan_csdn/article/details/74932682)


