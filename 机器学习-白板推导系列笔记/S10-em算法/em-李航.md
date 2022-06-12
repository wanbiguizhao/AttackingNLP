使用李航的例子进行学习。

EM算法就是含有隐变量的概率模型参数估计的最大似然方法。

尝试使用EM算法评估一下李航书中P155页的例子。

例9.1（三个硬币），假设有3枚硬币，分别记作A,B,C,这些硬币正面出现的概率的为π，p，q，进行如下抛掷硬币实验，先抛硬币A，然后根据结果选出硬币B或者硬币C正面，正面选择B，反面选择C；然后掷硬币的，出现正面记作1，出现反面选择0；重复n(=10)此实验: 1,1,0,1,0,0,1,0,1,1

问如何估计三硬币的模型参数?

单次抛硬币的概率模型为
$
\begin{equation}
\begin{aligned}
&P(y|\theta)\\
&=\sum_zP(y,z|\theta)\\
&=\sum_zP(z|\theta)P(y|z,\theta) \\
\end{aligned}
\end{equation}
$

隐形数据变量Z表示，抛掷硬币A时的结果。

$\theta=(\pi,p,q)$



$p(y,z|\theta)=\pi^z(1-\pi)^{1-z} [p^{yz}(1-p)^{(1-y)z}+q^{y(1-z)}(1-q)^{(1-y)(1-z)}-1] $

验证:将(y,z)=(0,0),(1,1),(0,1),(1,0)依次代入上面公式可得：
$
\begin{equation}
\begin{aligned}
&P(y=0,z=0|\theta)\\
&=(1-\pi)(1-q)\\
&P(y=0,z=1|\theta)\\
&=\pi(1-p)\\
&P(y=1,z=0|\theta)\\
&=(1-\pi)q\\
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

边缘概率分布
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
&\sum_z logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})\\
&=\prod_{i}^n\log p(y_i,z_1,z_2,..zn=0,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=0,0,\cdots,0|y_i,\theta^t) + \prod_{i}^n\log p(y_i,z_1,z_2,..zn=1,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,0,\cdots,0|y_i,\theta^t) + \cdots +  \prod_{i}^n\log p(y_i,z_1,z_2,..zn=1,1,\cdots,1|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,1,\cdots,1|y_i,\theta^t) 有2^n的和 \\
&=\log\sum_{i}^np(y_i,z_1,z_2,..zn=0,0,\cdots,0|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=0,0,\cdots,0|y_i,\theta^t) +...+ \log\sum_{i}^np(y_i,z_1,z_2,..zn=1,1,\cdots,1|\theta) \cdot \prod_{i}^np(z_1,z_2,..zn=1,1,\cdots,1|y_i,\theta^t)
\end{aligned}
\end{equation}
$
$Z=(z_1,z_2,...,z_n) $  
$Ez[logP(Y,Z|\theta)P(Z|Y,\theta^{(i)})]$对应的z的序列，是$2^n 的可能，n个0或者1组成的序列$ 感觉求不出来结果啊,计算的难度太大了。

需要分别对$\theta=(\pi,p,q)$求偏导，并对偏导计算得到零。