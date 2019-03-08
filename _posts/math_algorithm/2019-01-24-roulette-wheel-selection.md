---
layout: post
title: 轮盘赌法
category: 数学和算法
keywords: 轮盘赌法
---

## 算法实现原理
[原文地址:https://blog.csdn.net/tjj1998/article/details/80182625](https://blog.csdn.net/tjj1998/article/details/80182625)

首先每次运行时调用随机函数[rand](https://www.baidu.com/s?wd=rand&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)()/RAND_MAX，生成一个0-1之间的随机数temp;   
再判断该随机数究竟落到了哪一块区域:   
1.i=1时，如果temp<=sum (P[0]),则返回i,否则i++   
2.i=k时，如果temp<=sum（P[0]+…+P[k]），则返回i,否则i++   
……   
3.当i=N时截止。

```
int RWS() {
    double m = 0;
    double r = (double)rand()/RAND_MAX; //r为0至1的随机数
    for (int i = 0; i < N; i++) {
    /**
     * 产生的随机数在m~m+P[i]间则认为选中了i，因此i被选中的概率是P[i]
     */
        m = m + P[i];
        if (r <= m) return i;
    }
}
```


## 测试代码

```
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<ctime>
#include<algorithm>
#define INF 99999999
#define N 4//与P中数字个数相同 
#define Time 1000//自定义运行次数 
using namespace std;
double P[]={0.1,0.2,0.3,0.4};//相加之和为1 
int RWS() {
    double m = 0;
    double r = (double)rand()/RAND_MAX; //r为0至1的随机数
    for (int i = 0; i < N; i++) {
    /**
     * 产生的随机数在m~m+P[i]间则认为选中了i，因此i被选中的概率是P[i]
     */
        m = m + P[i];
        if (r <= m) return i;
    }
}
int main(){
    srand(time(0));
    int a[5];
    memset(a,0,sizeof(a));
    for(int i=0;i<Time;i++){
        int temp=RWS();
        a[temp]++;
    } 
    for(int i=0;i<N;i++){
        double temp=a[i]*1.0/Time;
        printf("%.3lf ",temp);
    } 
    return 0;
}
```

## 参考文档
[https://blog.csdn.net/zengzeyu/article/details/72627836](https://blog.csdn.net/zengzeyu/article/details/72627836)