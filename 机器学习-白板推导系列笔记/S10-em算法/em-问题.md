# 三个硬币的参数估计问题
## 一 问题描述
假设有3枚硬币，分别记作A,B,C,这些硬币正面出现的概率的为π，p，q，进行如下抛掷硬币实验，先抛硬币A，然后根据结果选出硬币B或者硬币C正面，正面选择B，反面选择C；然后掷硬币的，出现正面记作1，出现反面选择0；重复n(=10)此实验: 
```
1,1,0,1,0,0,1,0,1,1
```

问题:如何估计三硬币的模型参数$\theta=(\pi,p,q)$?





随机变量y表示观测的变量，表示依次实验观测的结果是1或者0；随机变量z是隐形变量，表示未记录的掷硬币A的结果。

观测数据表示为$\vec{Y}=(y_1,y_2,...,y_n)^T,未观测数据\vec{Z}=(z_1,z_2,...z_n)^T$

-----
## 二 已知的一些概率公式


### 单轮抛硬币的观测结果模型为：
$
\begin{equation}
\begin{aligned}
&P(y|\theta)\\
&=\sum_zP(y,z|\theta)\\
&=\sum_zP(z|\theta)P(y|z,\theta) \\
\end{aligned}
\end{equation}
$
$
\begin{equation}
\begin{aligned}
&p(y|\theta)\\
&=\pi^y(1-p)^{1-y}+(1-\pi)q^y(1-q)^{1-y}
\end{aligned}
\end{equation}
$





### y和z的联合概率分布公式如下



$
\begin{equation}
\begin{aligned}
&p(y,z|\theta)\\
&=\pi^z(1-\pi)^{1-z} [p^{yz}(1-p)^{(1-y)z}+q^{y(1-z)}(1-q)^{(1-y)(1-z)}-1]\\
\end{aligned}
\end{equation}$




验证:将(y,z)=(0,0),(1,1),(0,1),(1,0)依次代入上面公式可得：
$
\begin{equation}
\begin{aligned}
&P(y=0,z=0|\theta)\\
&=(1-\pi)(1-q)\\
\end{aligned}
\end{equation}$

$
\begin{equation}
\begin{aligned}
&P(y=0,z=1|\theta)\\
&=\pi(1-p)\\
\end{aligned}
\end{equation}
$
$
\begin{equation}
\begin{aligned}
&P(y=1,z=0|\theta)\\
&=(1-\pi)q\\
\end{aligned}
\end{equation}
$
$
\begin{equation}
\begin{aligned}
&P(y=1,z=1|\theta)\\
&=\pi p\\
\end{aligned}
\end{equation}
$

$
\begin{equation}
\begin{aligned}
p(y|\theta)\\
&=\pi^y(1-p)^{1-y}+(1-\pi)q^y(1-q)^{1-y}
\end{aligned}
\end{equation}
$

### z的边缘概率分布
$p(z|y,\theta)=\frac {p(y,z|\theta)}{p(y|\theta)} $

$
\begin{equation}
\begin{aligned}
&p(z|y,\theta)\\
&=\frac {p(y,z|\theta)}{p(y|\theta)}\\
&=\frac {\pi^z(1-\pi)^{1-z} [p^{yz}(1-p)^{(1-y)z}+q^{y(1-z)}(1-q)^{(1-y)(1-z)}-1]}{\pi p^y(1-p)^{1-y}+(1-\pi)q^y(1-q)^{1-y}}\\
\end{aligned}
\end{equation}
$

------
## 三评估参数 $\theta=(\pi , p ,q )$

常用的最大似然估计的算法
$\widehat{\theta}=\mathop{argmax}\limits_{\theta} \log P(\vec{Y}|\theta)$没有解析,只能通过EM算法迭代求解，EM算法https://en. wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm 主要分为两步：

第一步为求出$Ez[logP(Y,Z|\theta)P(Z|Y,\theta^{(t)})] \theta^{(t)} 是一个迭代参数，此时可以认为是常量$


第二步,在第一步的基础上，找出使$Ez最大化的\theta$

-----
以下是已知的一个公式。
$
\begin{equation}
\begin{aligned}\\
&logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})\\
&=\prod_{i}^n\log p(y_i,z_i|\theta) \cdot \prod_{i}^np(z_i|y_i,\theta^t)\\
&=\log\sum_{i}^np(y_i,z_i|\theta) \cdot \prod_{i}^np(z_i|y_i,\theta^t)
\end{aligned}
\end{equation}
$


$
\begin{equation}
\begin{aligned}\\
&E_z[logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})]\\
&=\sum_z logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})\\
&=\prod_{i}^n\log p(y_i,z_1,z_2,..zn=0,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=0,0,\cdots,0|y_i,\theta^t) + \prod_{i}^n\log p(y_i,z_1,z_2,..zn=1,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,0,\cdots,0|y_i,\theta^t) + \cdots +  \prod_{i}^n\log p(y_i,z_1,z_2,..zn=1,1,\cdots,1|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,1,\cdots,1|y_i,\theta^t) 有2^n的和 \\
&=\log\sum_{i}^np(y_i,z_1,z_2,..zn=0,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=0,0,\cdots,0|y_i,\theta^t) +...+ \log\sum_{i}^np(y_i,z_1,z_2,..zn=1,1,\cdots,1|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,1,\cdots,1|y_i,\theta^t)
\end{aligned}
\end{equation}
$
$\vec{Z}=(z_1,z_2,...,z_n)^T $ 表示 
$Ez[logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})]中 Z的可能序列(n个0或者1组成的序列),序列个数为2^n个$ 当n=10时，$E_z$共计有1024项求和. 

```
当前遇到的问题是
1. EM第一步的问题：求Ez的期望的项太多，没有办法展开，n=10时，就有1024项求和项，没有办法计算出真正的函数式。

2. EM第二步的问题：第一步计算很难推导出来函数式，没有办法针对（π，p，q）进行求偏单。

3. 现在的情况下第一步的函数式随着n的变化而变化，没有办法通过编程自动求解。
```

```
我想寻求的帮助：
数学领域中有没有相关三个硬币的相关教程或者论文，或者应该有些前沿的资料。
```
