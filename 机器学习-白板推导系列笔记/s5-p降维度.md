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
# P24 最大投影方差
需要找到方差最大的点，方差大的话，比较容易分类。
假设投影的向量已经找到。

$||\vec{u_1}||=1$

$\vec(x_i-\vec{\overline{x}})$在$\vec{u_1}$方向上的投影距离为为：$(x_i-\vec{\overline{x}})^{T}\cdot \vec{u_{1}}$

整体的方差和为为:

$J=\sum\limits_{i=1}^N[\vec(x_i-\vec{\overline{x}})^{T}\cdot \vec{u_{1}}]^2\\
=\sum\limits_{i=1}^N[\vec{u_{1}}^T \vec(x_i-\vec{\overline{x}})\vec(x_i-\vec{\overline{x}})^{T} \vec{u_{1}} ]\\
=\vec{u_{1}}^T\sum\limits_{i=1}^N\vec(x_i-\vec{\overline{x}})\vec(x_i-\vec{\overline{x}})^{T}\vec{u_{1}}\\
=N\vec{u_{1}}^TS\vec{u_{1}}$

最大方差问题转换为：


$ J=\frac{1}{N}\sum\limits_{i=1}^N\sum\limits_{j=1}^q((x_i-\overline{x})^Tu_j)^2 $

$=\sum\limits_{j=1}^qu_j^TSu_j  , s.t.  u_j^Tu_j=1 $


利用拉格朗日乘子优化进行求解：

$ \mathop{argmax}{u_j}L(u_j,\lambda)=\mathop{argmax}{u_j}u_j^TSu_j+\lambda(1-u_j^Tu_j) $

$ Su_j=\lambda u_j $


PCA 先做特征空间的重构，求出协方差矩阵$S_{p \times p}$的q个特征值，作为主成因。

困惑：特征值越到，对于结果的影响越明显？

## TODO: 需要学习矩阵求导公式。

## P25 最小重构距离
样本的中心化工作：

向量重构公式为：

$\vec{x_i}=(\vec{x_i}\cdot \vec{u_1})\vec{u_1} + (\vec{x_i}\cdot \vec{u_2})\vec{u_2}+....+ (\vec{x_i}\cdot \vec{u_2})\vec{u_p} $
$\vec{x_i}$

$=\sum\limits_{k=1}^p(\vec{x_i}\cdot \vec{u_2})\vec{u_k} $

重构的，从p个$\vec{u}$总选取q个向量。

$\hat{\vec{x_{i}}}=\sum\limits_{k=1}^q(\vec{x_i}\cdot \vec{u_k})\vec{u_k}$


$ J=\frac{1}{N}\sum\limits_{i=1}^N\sum\limits_{j=q+1}^p((x_i-\overline{x})^Tu_j)^2 = \sum\limits_{j=q+1}^pu_j^TSu_j\ ,s.t. u_j^Tu_j=1 $

```
核心都是找到样本方差矩阵S对应的特征值和特征向量，进行降维处理。最大投影分析：找最大的特征值。最小重构代价：删除掉最小的几个特征值。
```

# P26 SVD
$HX$ 表示的是任意一个样本点转化为:$\vec(x_i-\vec{\overline{x}})$ 点。


# P27 概率角度PCA分析。
线性高斯变化，这个以后再好好听吧。