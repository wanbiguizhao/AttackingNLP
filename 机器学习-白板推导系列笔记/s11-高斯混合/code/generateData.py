from distutils.debug import DEBUG
from hashlib import md5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

fig = plt.figure()
ax = plt.axes(projection='3d')
cov1 = np.mat("0.3 0 0;0 0.1 0;0 0 0.4 ") #协方差矩阵
cov2 = np.mat("0.2 0 0;0 0.3 0;0 0 0.15 ")# 协方差矩阵
mu1 = np.array([1.1, 0.5, 0.25])
mu2 = np.array([2.5, 1.2, 0.05])

sample = np.zeros((100, 3))
sample[:50, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=50)
sample[50:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=50)
np.savetxt("sample.data", sample)

plt.plot(sample[:50, 0], sample[:50, 1],sample[:50, 2], "bo")
plt.plot(sample[50:, 0], sample[:50, 1],sample[50:, 2], "rs")
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.scatter3D(sample[:50, 0], sample[:50, 1], sample[:50, 2], c=sample[:50, 0], cmap='Greens');
#ax.scatter3D(sample[50:, 0], sample[:50, 1],sample[50:, 2], c=sample[50:, 0], cmap='Reds');
ax.scatter3D(sample[:50, 0], sample[:50, 1], sample[:50, 2],  cmap='Greens');
ax.scatter3D(sample[50:, 0], sample[:50, 1],sample[50:, 2], cmap='viridis');
ax.scatter3D(sample[:50, 0]*0.7+0.3*sample[50:, 0], sample[:50, 1]*0.7+0.3*sample[50:, 1],sample[50:, 2]*0.7+0.3*sample[50:, 2], cmap='Blacks');
ax.legend()
plt.show()

DEBUG=False
def getData():
    # 2个高斯混合分布。
    cov1 = np.mat("0.3 0 0;0 0.1 0;0 0 0.4 ") #协方差矩阵
    cov2 = np.mat("0.2 0 0;0 0.3 0;0 0 0.15 ")# 协方差矩阵
    mu1 = np.array([1.1, 0.5, 0.25])
    mu2 = np.array([2.5, 1.2, 0.05])
    K1 = np.zeros((100, 3))
    K2 = np.zeros((100,3))
    K1 = np.random.multivariate_normal(mean=mu1, cov=cov1, size=100)
    K2 = np.random.multivariate_normal(mean=mu2, cov=cov2, size=100)
    MData=0.3*K1+0.7*K2 
    if DEBUG:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(K1[:,0],K1[:,1],K1[:,2],  cmap='Greens');
        ax.scatter3D(K2[:,0],K2[:,1],K2[:,2], cmap='viridis');
        ax.scatter3D(MData[:,0],MData[:,1],MData[:,2], cmap='Blacks');
        ax.legend()
        plt.show()
    return MData

if __name__=="__main__":
    getData()