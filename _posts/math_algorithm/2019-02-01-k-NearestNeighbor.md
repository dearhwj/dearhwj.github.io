---
layout: post
title: k近邻算法-java实现
category: 数学和算法
keywords: 锦标赛选择法
---

## 正文
一 . K-近邻算法（KNN）概述 

最简单最初级的分类器是将全部的训练数据所对应的类别都记录下来，当测试对象的属性和某个训练对象的属性完全匹配时，便可以对其进行分类。但是怎么可能所有测试对象都会找到与之完全匹配的训练对象呢，其次就是存在一个测试对象同时与多个训练对象匹配，导致一个训练对象被分到了多个类的问题，基于这些问题呢，就产生了KNN。

KNN是通过测量不同特征值之间的距离进行分类。它的的思路是：如果一个样本在特征空间中的k个最相似(即特征空间中最邻近)的样本中的大多数属于某一个类别，则该样本也属于这个类别。K通常是不大于20的整数。KNN算法中，所选择的邻居都是已经正确分类的对象。该方法在定类决策上只依据最邻近的一个或者几个样本的类别来决定待分样本所属的类别。

下面通过一个简单的例子说明一下：如下图，绿色圆要被决定赋予哪个类，是红色三角形还是蓝色四方形？如果K=3，由于红色三角形所占比例为2/3，绿色圆将被赋予红色三角形那个类，如果K=5，由于蓝色四方形比例为3/5，因此绿色圆被赋予蓝色四方形类。

![](https://images0.cnblogs.com/blog2015/771535/201508/041623504236939.jpg)

由此也说明了KNN算法的结果很大程度取决于K的选择。

在KNN中，通过计算对象间距离来作为各个对象之间的非相似性指标，避免了对象之间的匹配问题，在这里距离一般使用欧氏距离或曼哈顿距离：

![](https://images0.cnblogs.com/blog2015/771535/201508/041625523458191.jpg)

同时，KNN通过依据k个对象中占优的类别进行决策，而不是单一的对象类别决策。这两点就是KNN算法的优势。

接下来对KNN算法的思想总结一下：就是在训练集中数据和标签已知的情况下，输入测试数据，将测试数据的特征与训练集中对应的特征进行相互比较，找到训练集中与之最为相似的前K个数据，则该测试数据对应的类别就是K个数据中出现次数最多的那个分类，其算法的描述为：

1）计算测试数据与各个训练数据之间的距离；

2）按照距离的递增关系进行排序；

3）选取距离最小的K个点；

4）确定前K个点所在类别的出现频率；

5）返回前K个点中出现频率最高的类别作为测试数据的预测分类。

**代码实现：**

[https://www.cnblogs.com/huaxingtianxia/p/7383051.html](https://www.cnblogs.com/huaxingtianxia/p/7383051.html#)


 
```
import java.util.*;

/**
* code by me
* <p>
* Data:2017/8/17 Time:16:40
* User:lbh
*/

public class  KNN {

/**
* KNN数据模型 
*/

public static class KNNModel  implements Comparable<KNNModel> { 

         public double a; 
          public double b; 
          public double c; 
          public double distince; 
          String type; 
          public KNNModel( double a,  double b,  double c, String type) { 
              this .a = a; 
              this .b = b; 
              this .c = c; 
              this .type = type; 
          } 
          /** 
           * 按距离排序 
           * 
           * @param arg 
           * @return 
           */ 
          @Override 
          public int compareTo(KNNModel arg) { 
              return Double.valueOf( this .distince).compareTo(Double.valueOf(arg.distince)); 
          } 
      } 

      /** 
       * 计算距离 
       * 
       * @param knnModelList 
       * @param i 
       */ 
      private static void calDistince(List<KNNModel> knnModelList, KNNModel i) { 
          double distince; 
          for (KNNModel m : knnModelList) { 
              distince = Math.sqrt((i.a - m.a) * (i.a - m.a) + (i.b - m.b) * (i.b - m.b) + (i.c - m.c) * (i.c - m.c)); 
              m.distince = distince; 
          } 

      } 

      /** 
       * 找出前k个数据中分类最多的数据 
       * 
       * @param knnModelList 
       * @return 
       */ 

      private static String findMostData(List<KNNModel> knnModelList) { 
          Map<String, Integer> typeCountMap =  new HashMap<String, Integer>(); 
          String type =  "" ; 
          Integer tempVal =  0 ; 
          // 统计分类个数 
          for (KNNModel model : knnModelList) { 
              if (typeCountMap.containsKey(model.type)) { 
                  typeCountMap.put(model.type, typeCountMap.get(model.type) +  1 ); 
              }  else { 
                  typeCountMap.put(model.type,  1 ); 
              } 
          } 

          // 找出最多分类 
          for (Map.Entry<String, Integer> entry : typeCountMap.entrySet()) { 
              if (entry.getValue() > tempVal) { 
                  tempVal = entry.getValue(); 
                  type = entry.getKey(); 
              } 
          } 
          return type; 
      } 

      /** 
       * KNN 算法的实现 
       * 
       * @param k 
       * @param knnModelList 
       * @param inputModel 
       * @return 
       */ 

      public static String calKNN( int k, List<KNNModel> knnModelList, KNNModel inputModel) { 
          System.out.println( "1.计算距离" ); 
          calDistince(knnModelList, inputModel); 
          System.out.println( "2.按距离（近-->远）排序" ); 
          Collections.sort(knnModelList); 
          System.out.println( "3.取前k个数据" ); 
          while (knnModelList.size() > k) { 
              knnModelList.remove(k); 
          } 
          System.out.println( "4.找出前k个数据中分类出现频率最大的数据" ); 
          String type = findMostData(knnModelList); 
          return type; 
      } 

      /**
       * 测试KNN算法 
       * 
       * @param args 
       */ 

      public static void main(String[] args) { 
          // 准备数据 
          List<KNNModel> knnModelList =  new ArrayList<KNNModel>(); 
          knnModelList.add( new KNNModel( 1.1 ,  1.1 ,  1.1 ,  "A" )); 
          knnModelList.add( new KNNModel( 1.2 ,  1.1 ,  1.0 ,  "A" )); 
          knnModelList.add( new KNNModel( 1.1 ,  1.0 ,  1.0 ,  "A" )); 
          knnModelList.add( new KNNModel( 3.0 ,  3.1 ,  1.0 ,  "B" )); 
          knnModelList.add( new KNNModel( 3.1 ,  3.0 ,  1.0 ,  "B" )); 
          knnModelList.add( new KNNModel( 5.4 ,  6.0 ,  4.0 ,  "C" )); 
          knnModelList.add( new KNNModel( 5.5 ,  6.3 ,  4.1 ,  "C" )); 
          knnModelList.add( new KNNModel( 6.0 ,  6.0 ,  4.0 ,  "C" )); 
          knnModelList.add( new KNNModel( 10.0 ,  12.0 ,  10.0 ,  "M" )); 
          // 预测数据 
          KNNModel predictionData =  new KNNModel( 5.1 ,  6.2 ,  2.0 ,  "NB" ); 
          // 计算 
          String result = calKNN( 3 , knnModelList, predictionData); 
          System.out.println( "预测结果：" +result); 

      } 