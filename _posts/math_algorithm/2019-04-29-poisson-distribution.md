---
layout: post
title: 如何通俗理解泊松分布
category: 数学和算法
keywords: 泊松分布
---

## 正文
[原文地址：https://blog.csdn.net/ccnt_2012/article/details/81114920](https://blog.csdn.net/ccnt_2012/article/details/81114920)



**1 甜在心馒头店**

公司楼下有家馒头店：

![](https://img-blog.csdn.net/20180720091046462?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

每天早上六点到十点营业，生意挺好，就是发愁一个事情，应该准备多少个馒头才能既不浪费又能充分供应？

老板统计了一周每日卖出的馒头（为了方便计算和讲解，缩小了数据）：

![\begin{array}{c|c} \qquad\qquad&\qquad销售\qquad\\\hline\color{SkyBlue}{周一}& 3 \\ \hline \color{blue}{周二}& 7 \\ \hline \color{orange}{周三}&4\\\hline \color{Goldenrod}{周四}&6\\ \hline \color{green}{周五}&5\\\end{array}\\](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20%5Cqquad%5Cqquad%26%5Cqquad%E9%94%80%E5%94%AE%5Cqquad%5C%5C%5Chline%5Ccolor%7BSkyBlue%7D%7B%E5%91%A8%E4%B8%80%7D%26%203%20%5C%5C%20%5Chline%20%5Ccolor%7Bblue%7D%7B%E5%91%A8%E4%BA%8C%7D%26%207%20%5C%5C%20%5Chline%20%5Ccolor%7Borange%7D%7B%E5%91%A8%E4%B8%89%7D%264%5C%5C%5Chline%20%5Ccolor%7BGoldenrod%7D%7B%E5%91%A8%E5%9B%9B%7D%266%5C%5C%20%5Chline%20%5Ccolor%7Bgreen%7D%7B%E5%91%A8%E4%BA%94%7D%265%5C%5C%5Cend%7Barray%7D%5C%5C)

均值为：

![\overline{X}=\frac{3+7+4+6+5}{5}=5\\](https://www.zhihu.com/equation?tex=%5Coverline%7BX%7D%3D%5Cfrac%7B3%2B7%2B4%2B6%2B5%7D%7B5%7D%3D5%5C%5C)

按道理讲均值是不错的选择（参见[如何理解最小二乘法](https://www.matongxue.com/madocs/818.html)？），但是如果每天准备5个馒头的话，从统计表来看，至少有两天不够卖，![40\%](https://www.zhihu.com/equation?tex=40%5C%25) 的时间不够卖：

![\begin{array}{c|c}\qquad\qquad&\qquad销售\qquad&\quad备货五个\\\hline\color{SkyBlue}{周一}& 3 \\\hline \color{blue}{周二}& 7&\color{red}{不够} \\ \hline \color{orange}{周三}&4\\ \hline \color{Goldenrod}{周四}&6&\color{red}{不够}\\\hline \color{green}{周五}&5\\\end{array}\\](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bc%7Cc%7D%5Cqquad%5Cqquad%26%5Cqquad%E9%94%80%E5%94%AE%5Cqquad%26%5Cquad%E5%A4%87%E8%B4%A7%E4%BA%94%E4%B8%AA%5C%5C%5Chline%5Ccolor%7BSkyBlue%7D%7B%E5%91%A8%E4%B8%80%7D%26%203%20%5C%5C%5Chline%20%5Ccolor%7Bblue%7D%7B%E5%91%A8%E4%BA%8C%7D%26%207%26%5Ccolor%7Bred%7D%7B%E4%B8%8D%E5%A4%9F%7D%20%5C%5C%20%5Chline%20%5Ccolor%7Borange%7D%7B%E5%91%A8%E4%B8%89%7D%264%5C%5C%20%5Chline%20%5Ccolor%7BGoldenrod%7D%7B%E5%91%A8%E5%9B%9B%7D%266%26%5Ccolor%7Bred%7D%7B%E4%B8%8D%E5%A4%9F%7D%5C%5C%5Chline%20%5Ccolor%7Bgreen%7D%7B%E5%91%A8%E4%BA%94%7D%265%5C%5C%5Cend%7Barray%7D%5C%5C)

你“甜在心馒头店”又不是小米，搞什么饥饿营销啊？老板当然也知道这一点，就拿起纸笔来开始思考。

**2 老板的思考**

老板尝试把营业时间抽象为一根线段，把这段时间用 ![T](https://www.zhihu.com/equation?tex=T) 来表示：

![](https://img-blog.csdn.net/2018072009112033?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

然后把周一的三个馒头（“甜在心馒头”，有褶子的馒头）按照销售时间放在线段上：

![](https://img-blog.csdn.net/20180720091134821?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

把 ![T](https://www.zhihu.com/equation?tex=T) 均分为四个时间段：

![](https://img-blog.csdn.net/2018072009114717?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

此时，在每一个时间段上，要不卖出了（一个）馒头，要不没有卖出：

![](https://img-blog.csdn.net/20180720091156857?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

在每个时间段，就有点像抛硬币，要不是正面（卖出），要不是反面（没有卖出）：

![](https://img-blog.csdn.net/20180720091209939?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![T](https://www.zhihu.com/equation?tex=T) 内卖出3个馒头的概率，就和抛了4次硬币（4个时间段），其中3次正面（卖出3个）的概率一样了。

这样的概率通过二项分布来计算就是：

![\binom{4}{3}p^3(1-p)^1\\](https://www.zhihu.com/equation?tex=%5Cbinom%7B4%7D%7B3%7Dp%5E3(1-p)%5E1%5C%5C)

但是，如果把周二的七个馒头放在线段上，分成四段就不够了：

![](https://img-blog.csdn.net/2018072009122362?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

从图中看，每个时间段，有卖出3个的，有卖出2个的，有卖出1个的，就不再是单纯的“卖出、没卖出”了。不能套用二项分布了。

解决这个问题也很简单，把 ![T](https://www.zhihu.com/equation?tex=T) 分为20个时间段，那么每个时间段就又变为了抛硬币：

![](https://img-blog.csdn.net/20180720091237705?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这样，![T](https://www.zhihu.com/equation?tex=T) 内卖出7个馒头的概率就是（相当于抛了20次硬币，出现7次正面）：

![\binom{20}{7}p^7(1-p)^{13}\\](https://www.zhihu.com/equation?tex=%5Cbinom%7B20%7D%7B7%7Dp%5E7(1-p)%5E%7B13%7D%5C%5C)

为了保证在一个时间段内只会发生“卖出、没卖出”，干脆把时间切成 ![n](https://www.zhihu.com/equation?tex=n) 份：

![\binom{n}{7}p^7(1-p)^{n-7}\\](https://www.zhihu.com/equation?tex=%5Cbinom%7Bn%7D%7B7%7Dp%5E7(1-p)%5E%7Bn-7%7D%5C%5C)

越细越好，用极限来表示：

![\lim_{n\to\infty}\binom{n}{7}p^7(1-p)^{n-7}\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7B7%7Dp%5E7(1-p)%5E%7Bn-7%7D%5C%5C)

更抽象一点，![T](https://www.zhihu.com/equation?tex=T) 时刻内卖出 ![k](https://www.zhihu.com/equation?tex=k) 个馒头的概率为：

![\lim_{n\to\infty}\binom{n}{k}p^k(1-p)^{n-k}\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7Bk%7Dp%5Ek(1-p)%5E%7Bn-k%7D%5C%5C)

**3 ![p](https://www.zhihu.com/equation?tex=p) 的计算**

“那么”，老板用笔敲了敲桌子，“只剩下一个问题，概率 ![p](https://www.zhihu.com/equation?tex=p) 怎么求？”

在上面的假设下，问题已经被转为了二项分布。二项分布的期望为：

![E(X)=np=\mu\\](https://www.zhihu.com/equation?tex=E(X)%3Dnp%3D%5Cmu%5C%5C)

那么：

![p=\frac{\mu}{n}\\](https://www.zhihu.com/equation?tex=p%3D%5Cfrac%7B%5Cmu%7D%7Bn%7D%5C%5C)

**4 泊松分布**

有了 ![p=\frac{\mu}{n}](https://www.zhihu.com/equation?tex=p%3D%5Cfrac%7B%5Cmu%7D%7Bn%7D)了之后，就有：

![\lim_{n\to\infty}\binom{n}{k}p^k(1-p)^{n-k}=\lim_{n\to\infty}\binom{n}{k}\left(\frac{\mu}{n}\right)^k(1-\frac{\mu}{n})^{n-k}\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7Bk%7Dp%5Ek(1-p)%5E%7Bn-k%7D%3D%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7Bk%7D%5Cleft(%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5Ek(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D)%5E%7Bn-k%7D%5C%5C)

我们来算一下这个极限：

![\begin{align}\lim_{n\to\infty}\binom{n}{k}\left(\frac{\mu}{n}\right)^k(1-\frac{\mu}{n})^{n-k}&= \lim_{n\to\infty}\frac{n(n-1)(n-2)\cdots(n-k+1)}{k!}\frac{\mu^k}{n^k}\left(1-\frac{\mu}{n}\right)^{n-k}\\ &=\lim_{n\to\infty}\frac{\mu^k}{k!}\frac{n}{n}\cdot\frac{n-1}{n}\cdots\frac{n-k+1}{n}\left(1-\frac{\mu}{n}\right)^{-k}\left(1-\frac{\mu}{n}\right)^n\end{align}\\](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%7D%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7Bk%7D%5Cleft(%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5Ek(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D)%5E%7Bn-k%7D%26%3D%20%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cfrac%7Bn(n-1)(n-2)%5Ccdots(n-k%2B1)%7D%7Bk!%7D%5Cfrac%7B%5Cmu%5Ek%7D%7Bn%5Ek%7D%5Cleft(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5E%7Bn-k%7D%5C%5C%20%26%3D%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cfrac%7B%5Cmu%5Ek%7D%7Bk!%7D%5Cfrac%7Bn%7D%7Bn%7D%5Ccdot%5Cfrac%7Bn-1%7D%7Bn%7D%5Ccdots%5Cfrac%7Bn-k%2B1%7D%7Bn%7D%5Cleft(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5E%7B-k%7D%5Cleft(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5En%5Cend%7Balign%7D%5C%5C)

其中：

![\lim_{n\to\infty}\frac{n}{n}\cdot\frac{n-1}{n}\cdots\frac{n-k+1}{n}\left(1-\frac{\mu}{n}\right)^{-k}=1\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cfrac%7Bn%7D%7Bn%7D%5Ccdot%5Cfrac%7Bn-1%7D%7Bn%7D%5Ccdots%5Cfrac%7Bn-k%2B1%7D%7Bn%7D%5Cleft(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5E%7B-k%7D%3D1%5C%5C)

![\lim_{n \to \infty}\left(1-\frac{\mu}{n}\right)^n = e^{-\mu}\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%20%5Cto%20%5Cinfty%7D%5Cleft(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5En%20%3D%20e%5E%7B-%5Cmu%7D%5C%5C)

所以：

![\lim_{n\to\infty}\binom{n}{k}\left(\frac{\mu}{n}\right)^k(1-\frac{\mu}{n})^{n-k}=\frac{\mu^k}{k!}e^{-\mu}\\](https://www.zhihu.com/equation?tex=%5Clim_%7Bn%5Cto%5Cinfty%7D%5Cbinom%7Bn%7D%7Bk%7D%5Cleft(%5Cfrac%7B%5Cmu%7D%7Bn%7D%5Cright)%5Ek(1-%5Cfrac%7B%5Cmu%7D%7Bn%7D)%5E%7Bn-k%7D%3D%5Cfrac%7B%5Cmu%5Ek%7D%7Bk!%7De%5E%7B-%5Cmu%7D%5C%5C)

上面就是泊松分布的概率密度函数，也就是说，在 ![T](https://www.zhihu.com/equation?tex=T) 时间内卖出 ![k](https://www.zhihu.com/equation?tex=k) 个馒头的概率为：

![P(X=k)=\frac{\mu^k}{k!}e^{-\mu}\\](https://www.zhihu.com/equation?tex=P(X%3Dk)%3D%5Cfrac%7B%5Cmu%5Ek%7D%7Bk!%7De%5E%7B-%5Cmu%7D%5C%5C)

一般来说，我们会换一个符号，让 ![\mu=\lambda](https://www.zhihu.com/equation?tex=%5Cmu%3D%5Clambda) ，所以：

![P(X=k)=\frac{\lambda^k}{k!}e^{-\lambda}\\](https://www.zhihu.com/equation?tex=P(X%3Dk)%3D%5Cfrac%7B%5Clambda%5Ek%7D%7Bk!%7De%5E%7B-%5Clambda%7D%5C%5C)

这就是教科书中的泊松分布的概率密度函数。

**5 馒头店的问题的解决**

老板依然蹙眉，不知道 ![\mu](https://www.zhihu.com/equation?tex=%5Cmu) 啊？

没关系，刚才不是计算了样本均值：

![\overline{X}=5\\](https://www.zhihu.com/equation?tex=%5Coverline%7BX%7D%3D5%5C%5C)

可以用它来近似：

![\overline{X}\approx\mu\\](https://www.zhihu.com/equation?tex=%5Coverline%7BX%7D%5Capprox%5Cmu%5C%5C)

于是：

![P(X=k)=\frac{5^k}{k!}e^{-5}\\](https://www.zhihu.com/equation?tex=P(X%3Dk)%3D%5Cfrac%7B5%5Ek%7D%7Bk!%7De%5E%7B-5%7D%5C%5C)

画出概率密度函数的曲线就是：

![](https://img-blog.csdn.net/20180720091300482?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

可以看到，如果每天准备8个馒头的话，那么足够卖的概率就是把前8个的概率加起来：

![](https://img-blog.csdn.net/20180720091309679?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

这样 ![93\%](https://www.zhihu.com/equation?tex=93%5C%25) 的情况够用，偶尔卖缺货也有助于品牌形象。

老板算出一脑门的汗，“那就这么定了！”

**6 二项分布与泊松分布**

鉴于二项分布与泊松分布的关系，可以很自然的得到一个推论，当二项分布的 ![p](https://www.zhihu.com/equation?tex=p) 很小的时候，两者比较接近：

![](https://img-blog.csdn.net/20180720091323860?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NjbnRfMjAxMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**7 总结**

这个故事告诉我们，要努力学习啊，要不以后馒头都没得卖。

生活中还有很多泊松分布。比如物理中的半衰期，我们只知道物质衰变一半的时间期望是多少，但是因为[不确定性原理](https://www.zhihu.com/question/27223172/answer/362337625)，我们没有办法知道具体哪个原子会在什么时候衰变？所以可以用泊松分布来计算。

还有比如交通规划等等问题。


