# -*- coding: utf-8 -*-
# ----------------------------------------------------
# Copyright (c) 2017, Wray Zheng. All Rights Reserved.
# Distributed under the BSD License.
# ----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import os,sys 
sys.path.append(".") 

from gmm import *
from generateData import getData

# 设置调试模式
DEBUG = True

# 载入数据
X=getData()
matX = np.matrix(X, copy=True)

# 模型个数，即聚类的类别个数
K = 2

# 计算 GMM 模型参数
mu, cov, alpha = GMM_EM(matX, K, 100)

# 根据 GMM 模型，对样本数据进行聚类，一个模型对应一个类别
N = X.shape[0]
# 求当前模型参数下，各模型对样本的响应度矩阵
gamma = getExpectation(matX, mu, cov, alpha)
# 对每个样本，求响应度最大的模型下标，作为其类别标识
category = gamma.argmax(axis=1).flatten().tolist()[0]
# 将每个样本放入对应类别的列表中
class1 = np.array([X[i] for i in range(N) if category[i] == 0])
class2 = np.array([X[i] for i in range(N) if category[i] == 1])
ax = plt.axes(projection='3d')
# 绘制聚类结果
plt.plot(class1[:, 0], class1[:, 1], class1[:, 2], 'rs', label="class1")
plt.plot(class2[:, 0], class2[:, 1],class2[:, 2], 'bo', label="class2")
plt.legend(loc="best")
plt.title("GMM Clustering By EM Algorithm")
plt.show()
print("over")