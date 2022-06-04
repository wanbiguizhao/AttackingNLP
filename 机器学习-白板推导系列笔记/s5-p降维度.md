1. 过拟合的表现形式？
两个误差，训练误差和泛化误差，当训练误差小，泛化误差大时，认为存在过拟合的情况。
## 过拟合
### 直接降维
岭回归
### 线性降维 
PCA
### 非线性降维
 Isomap，LLE
2. 数据稀疏和数据分配不均匀。

# P23 样本均值和样本方差矩阵
## 数学知识
$\vec{x_i}=\left[\begin{array}{c} x_{i1} \\x_{i2} \\... \\ x_{ip} \end{array}\right]$ 是p维的列向量

样本集合:X由n个样本数据，每个样本数据由p列属性。

$X_{n\times p}=[\vec{x_1},\vec{x_2},...,\vec{x_n}]^T=\left[\begin{array}{c}\vec{x_1}^T \\\vec{x_2}^T \\... \\ \vec{x_n}^T \end{array}\right]_{n \times  p}$

$I_{N,1}=\left[\begin{array}{c} 1 \\1 \\... \\ 1 \end{array}\right]_N$ 表示N维度列向量

$\vec{\overline{x}}=\frac{1}{N}\sum\limits_{i=1}^N\vec{x_i}$

$\vec{\overline{x}}I_{N,1}^{T}= \vec{\overline{x}}I_{1,N}=[\vec{\overline{x}},\vec{\overline{x}},...,\vec{\overline{x}}]_{p \times N}$

$(X_{n\times p})^{T}=(X^{T})_{p \times n}$

$(X^{T})I_{N,1}=\left[\begin{array}{c} \sum\limits_{i=1}^N\vec{x_{i1}} \\ \sum\limits_{i=1}^N\vec{x_{i2}} \\ ... \\ \sum\limits_{i=1}^N\vec{x_{ip}}   \end{array}\right]$=$N\vec{\overline{x}}$

$S$
$=\frac{1}{N}\sum\limits_{i=1}^N(\vec{x_i}-\vec{\overline{x}})(\vec{x_i}-\vec{\overline{x}})^T$

$=\frac{1}{N}(\vec{x_1}-\vec{\overline{x}},\vec{x_2}-\vec{\overline{x}},\cdots,\vec{x_N}-\vec{\overline{x}})(\vec{x_1}-\vec{\overline{x}},\vec{x_2}-\vec{\overline{x}},\cdots,\vec{x_N}-\vec{\overline{x}})^T$

$=\frac{1}{N}[ [\vec{x_1},\vec{x_2},...,\vec{x_n}]_{p \times N}-[\vec{\overline{x}},\vec{\overline{x}},...,\vec{\overline{x}}]_{p \times N} ](\vec{x_1}-\vec{\overline{x}},\vec{x_2}-\vec{\overline{x}},\cdots,\vec{x_N}-\vec{\overline{x}})^T$

$=\frac{1}{N}[X^{T}- \vec{\overline{x}}I_{1,N}][X^{T}- \vec{\overline{x}}I_{1,N}]^T$

$=\frac{1}{N}[X^{T}- \frac{1}{N}X^TI_{N, 1}I_{1,N}][X^{T}- \frac{1}{N}X^TI_{N, 1}I_{1,N}]^T$

$=\frac{1}{N}[X^{T}(E_n- \frac{1}{N}I_{N, 1}I_{1,N})][X^{T}(E_n- \frac{1}{N}I_{N, 1}I_{1,N})]^T$

$=\frac{1}{N}[X^{T}(E_n- \frac{1}{N}I_{N, 1}I_{1,N})] [(E_n- \frac{1}{N}I_{N, 1}I_{1,N})]^T(X^{T})^{T}$

$=\frac{1}{N}X^{T}(E_n- \frac{1}{N}I_{N, 1}I_{1,N})(E_n- \frac{1}{N}I_{N, 1}I_{1,N})^TX$


令 $H_{n \times n}=(E_n- \frac{1}{N}I_{N, 1}I_{1,N})$
则

$S=\frac{1}{N}X^{T}(E_n- \frac{1}{N}I_{N, 1}I_{1,N})(E_n- \frac{1}{N}I_{N, 1}I_{1,N})^TX$

$=\frac{1}{N}X^{T}H_{n \times n}H_{n \times n}^TX$



注意：

------


$H_{n \times n}=H_{n \times n}^T$

证明：
 $H_{n \times n}^T=(E_n- \frac{1}{N}I_{N, 1}I_{1,N})^T$

 $=E_n- \frac{1}{N}I_{1,N}^TI_{N, 1}$^T

 $= E_n- \frac{1}{N}I_{N, 1}I_{1,N}$
 $= H_{n \times n}$

----

$H_{n \times n} H_{n \times n}=H_{n \times n}$

证明：
$H_{n \times n} H_{n \times n}$

$=(E_n- \frac{1}{N}I_{N, 1}I_{1,N})(E_n- \frac{1}{N}I_{N, 1}I_{1,N}) $

$=E_nE_n- \frac{1}{N}E_nI_{N, 1}I_{1,N}-\frac{1}{N}I_{N, 1}I_{1,N}E_n+ \frac{1}{N^2}I_{N, 1}I_{1,N}I_{N, 1}I_{1,N} $

$=E_n- \frac{2}{N}I_{N, 1}I_{1,N}+ \frac{1}{N^2}I_{N, 1} \cdot  N\cdot I_{1,N} $

$=E_n- \frac{1}{N}I_{N, 1}I_{1,N}$