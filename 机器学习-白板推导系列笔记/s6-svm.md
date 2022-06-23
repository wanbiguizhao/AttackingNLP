# SVM算法
- 硬间隔 hard-margin svm
- 软间隔 soft-margin svm
- 核函数 kernel svm

N个任一一个样本点到|$\vec{w}^T\vec{x}+\vec{b}$|平面的距离L,
核心是找到max(min(L))的平面。

硬间隔是假设所有的点一定可以找到一个平面似的数据可分。

## 软间隔
-----

运行数据是可以不可分的。



$\vec{x}_k,y_{k}，\lambda_{i}$如何找到呢？

----

## 仿射变换与仿射函数：
从$R^n$到$R^m$的映射$\vec{x}_{n\times 1}\rightarrow A_{m \times n}\vec{x}_{n\times 1}+\vec{b}_{m \times 1}$，称为仿射变换，当m=1是，称上述的仿射变换为仿射函数。

# 指示函数


# 代码测试
可以使用高斯分布，生成一些数据，然后进行分类工作。