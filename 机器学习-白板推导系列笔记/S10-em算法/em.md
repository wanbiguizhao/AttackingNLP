$\theta^{(t+1)}=\mathop{argmax}\limits_{\theta}\int_z\log   [p(\vec{x},\vec{z}|\theta)] \cdot p(\vec{z}|\vec{x},\theta^t)dz$

$p(z|x,\theta^t)$ 后验概率
关键是弄明白

$\theta$的参数代表的是什么？

z代表的分布是什么？

核心点就是在于证明如何保证迭代过程中？

确保每一步迭代过程中：

$\log p(x|\theta^t)\le\log p(x|\theta^{t+1})$

---

$\log p(\vec{x}|\vec{\theta})=\log [ p(\vec{x},\vec{z}|\vec{\theta})/p(\vec{z}|\vec{x},\vec{\theta}) ] $

$\log p(\vec{x}|\vec{\theta})=\log [ p(\vec{x},\vec{z}|\vec{\theta})]-\log[p(\vec{z}|\vec{x},\vec{\theta}) ] $

左右两边同时乘以$ p(\vec{z}|\vec{x},\vec{\theta^t})$ ,公式调整:

$\begin{equation}\begin{aligned}
&\log p(\vec{x}|\vec{\theta}) \cdot  p(\vec{z}|\vec{x},\vec{\theta^t}) \\
&= p(\vec{z}|\vec{x},\vec{\theta^t}) \cdot \log [ p(\vec{x},\vec{z}|\vec{\theta})/p(\vec{z}|\vec{x},\vec{\theta})]\\
&= p(\vec{z}|\vec{x},\vec{\theta^t}) \cdot \log p(\vec{x},\vec{z}|\vec{\theta})  - p(\vec{z}|\vec{x},\vec{\theta^t}) \cdot \log p(\vec{z}|\vec{x},\vec{\theta}) \\
\end{aligned}
\end{equation}
$


左右两边对z就行求积分
$\begin{equation}\begin{aligned}
&left\\
&=\int_z \log p(\vec{x}|\vec{\theta}) \cdot  p(\vec{z}|\vec{x},\vec{\theta^t}) dz\\
&=\log p(\vec{x}|\vec{\theta})\cdot\int_z p(\vec{z}|\vec{x},\vec{\theta^t}) dz\\
&=\log p(\vec{x}|\vec{\theta}) 
\end{aligned}
\end{equation}
$

右边的公式积分:
$\begin{equation}\begin{aligned}
&right\\
&=\int_z   p(\vec{z}|\vec{x},\vec{\theta^t}) \cdot \log p(\vec{x},\vec{z}|\vec{\theta})  dz  -\int_zp(\vec{z}|\vec{x},\vec{\theta^t}) \cdot \log p(\vec{z}|\vec{x},\vec{\theta})dz\\
&=Q(\theta,\theta^t)-H(\theta,\theta^t)\\
\end{aligned}
\end{equation}
$

先讨论$Q(\theta,\theta^t)$根据定义：

$\vec{\theta}^{(t+1)}=\mathop{argmax}\limits_{\theta}\int_{\vec{z}}\log [p(\vec{x},\vec{z}|\vec{\theta})]p(\vec{z}|\vec{x},{\vec{\theta}^t})d\vec{z}   (此时\theta^t是一个常数(向量))$


$Q(\vec{\theta}^{t+1},\vec{\theta}^t)\ge Q(\vec{\theta},\vec{\theta}^t) $
所以



$Q(\vec{\theta}^{t+1},\vec{\theta}^t)\ge Q(\vec{\theta}^t,\vec{\theta}^t) $

现在证明：

要证 $\log p(x|\theta^t)\le\log p(x|\theta^{t+1})$，需证：$H(\theta^t,\theta^t)\ge H(\theta^{t+1},\theta^t)$：



$
\begin{equation}
\begin{align}
&H(\theta^{t+1},\theta^t)-H(\theta^{t},\theta^t)\\
&=\int_zp(\vec{z}|\vec{x},\theta^{t}) \cdot \log p(\vec{z}|\vec{x},\theta^{t+1})dz -\int_zp(\vec{z}|\vec{x},\theta^t)\log p(\vec{z}|\vec{x},\theta^{t})dz\\
&=\int_zp(\vec{z}|\vec{x},\theta^{t}) \cdot \log \frac{p(\vec{z}|\vec{x},\theta^{t+1})}{p(\vec{z}|\vec{x},\theta^{t})}dz \\
&=-KL(p(\vec{z}|\vec{x},\theta^t),p(\vec{z}|\vec{x},\theta^{t+1}))
\end{align}
\end{equation}
$
所以当满足:$\theta^{(t+1)}=\mathop{argmax}\limits_{\theta}\int_z\log   [p(\vec{x},\vec{z}|\theta)] \cdot p(\vec{z}|\vec{x},\theta^t)dz$ 时可以保证：

 $\log p(\vec{x}|\theta^t)\le\log p(x|\theta^{t+1})$

---

 # P61 
教程的问题E步骤和M没有具体的演示，我都不清楚怎么求出来E。
这个时候要看李航的例子了。
视频中没有给出，有效证明按照EM的步骤，可以使的x的边缘分布在这种迭代的情况下越来越大。
 ## E 步的操作步骤
计算 $\log p(x,z|\theta)$ 在概率分布 $p(z|x,\theta^t)$ 下的期望

 ## M 步的操作步骤

计算使这个期望最大化的参数得到下一个 EM 步骤的输入
