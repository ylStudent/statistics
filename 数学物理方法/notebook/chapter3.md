## 复变函数级数理论
### 1. 复变项级数
形如$f_1 + f_2 + ... + f_k = \sum_{k=1}^{\infty}f_k$的级数（其中$f_k = u_k + iv_k$）称为复级数。
$$ \sum_{k=1}^{\infty} f_k = \sum_{k=1}^{\infty}u_k + i\sum_{k=1}^{\infty}v_k $$

部分和$F_n = \sum_{k=1}^{n} f_k$，若$lim_{n->\infty}F_n = F$存在且有限，则称$\sum_{k=1}^{\infty} f_k $收敛于$F = u + iv$，即 
$$ \sum_{k=1}^{\infty} u_k = u$$
$$ \sum_{k=1}^{\infty} v_k = v$$

**柯西判据**
对于任意$\epsilon > 0$，总存在正整数$N$，当$n > N$，有$|F_{n+p} - F_n| = |f_{k+1} + f_{k+2} + ... + f_{k+p}| < \epsilon$，对任意$p>1$成立，则$\sum_{k=1}^{\infty} f_k$一定收敛。
当$p=1$时，$lim_{k \rightarrow \infty}|f_{k+1}| = 0 \Rightarrow lim_{k \rightarrow \infty}|f_{k}| = 0 $ （必要条件）

**莱布尼兹判据**
如果一个交错级数，其通项在$lim_{n\rightarrow \infty}f_n = 0$，收敛。

**绝对收敛性**
若$\sum_{k=1}^{\infty} |f_k| $收敛，则称$\sum_{k=1}^{\infty} f_k $绝对收敛，且原级数本身亦收敛，因：$|f_{k+1} + ... + f_{k+p}| < |f_{k+1}| + |f_{k+2}| + ... + |f_{k+p}|$（柯西判据）

**绝对收敛级数的性质**  
任意交换或改变次序而得到新的级数收敛，且其和不变。  

两个绝对收敛的级数，可逐项相乘，仍收敛。  

**比值判别法（达朗贝尔判别法）**  
若$\sum_{k=1}^{\infty}f_k$的通项$f_k(k=1,2...)$满足：$$\lim_{k \rightarrow \infty} \frac{f_{k+1}}{f_k} = l$$  
若 $l < 1$，则$\sum_{k=1}^{\infty}f_k$绝对收敛； 若 $l > 1$，则$\sum_{k=1}^{\infty}f_k$发散； 当 $l = 1$，则$\sum_{k=1}^{\infty}f_k$的敛散性无法判断。

**高斯判别法**  
对于$ \sum_{k=1}^{\infty} f_k $，若$\frac{f_k}{f_{k+1}} = 1 + \frac{\mu}{k} + O(\frac{1}{k^{\lambda}}), \lambda > 0$

若$Re\ \mu > 1$，则$\sum_{k=1}^{\infty}f_k$绝对收敛

若$Re\ \mu <= 1$，则$\sum_{k=1}^{\infty}f_k$发散

证明参考到了**P级数**

**柯西根值判别法**  
对$\sum_{k=1}^{\infty} f_k $ 若$lim_{k \rightarrow \infty} \sqrt[k]{|f_k|}$，则

当 $ r > 1$，$\sum_{k=1}^{\infty} f_k$绝对收敛。

当$ r < 1$，$\sum_{k=1}^{\infty} f_k$发散。

当$ r = 1$，$\sum_{k=1}^{\infty} f_k$的敛散性

**复变函数项级数**：形如$\sum_{k=1}^{\infty}f_k(z)$的级数。    

**一致收敛性**：如在$\sigma$上存在函数$F(z)$，对任意$\epsilon > 0$，存在无关于$z$的自然数$N$，当$n > N$时，对任意：$$ |F(z) - F_n(z)| < \epsilon$$
则称$\sum_{k=1}^{\infty} f_k(z)$一致收敛于$F(z)$

一致收敛的复变函数项级数的性质，对$\sum_{k=1}^{\infty} f_k(z)$（一致收敛于$\sigma$）

**1. 连续性**：若$f_k(z)$在$\sigma$上连续，则$\sum_k^{\infty} f_k(z) = F(z)$在$\sigma$上亦连续。

**2**. 若$f_k(z)$在$l \in \sigma$曲线上连续可积，则$\sum_{k=1}^{\infty} f_k(z)$可逐项积分。$$ \int_l F(z)dz = \int_l(\sum_{k=1}^{\infty} f_k(z)dz$$

**3.** 若$f_k(z)$ 在$\sigma$区域解析，且级数在$\sigma$内任一闭区域$\sigma'$一致收敛，则$\sum_{k=1}^{\infty} f_k(z) = F(z)$可逐项求导且$F(z)$上解析。$$ F_{(z)}^{(n)} = \sum_{k=1}^{\infty} f_k^{n}(z)$$

**一致收敛法判别法**：

**M判别法**：   
一致而且绝对收敛的一个充分而不必要条件。
若在闭区域$\hat{\sigma} = \sigma + l$内$|f_k(z)| \leq M_k$（与$z$无关），而$\sum_{k=1}^{\infty} M_k$收敛，则$\sum_{k=1}^{\infty} f_k(z)$在$\sigma$上绝对而且一致收敛。

### 幂级数
形如$\sum_{k=0}^{\infty} a_k(z-b)^k$的级数。它是以$b$为中心的幂级数，$a_k(k=0, 1, 2, ...)$是复常数。  
判定幂级数敛散性的定理——**阿贝尔定理(Abel)**

若幂级数$\sum_{k=0}^{\infty} a_k(z-b)^k$在某点$z=z_0$处收敛，则$z$在$|z-b| < |z_0 - b|$ 内绝对收敛，在更小的闭圆$|z-b| \leq \rho$一致收敛。

**收敛圆及收敛半径**：

$R = lim_{k \rightarrow \infty} \frac{a_{k+1}}{a_k}$ R为收敛不收敛的分界线。

由柯西的根值求法也可以得到半径：
$$ R = lim_{k \rightarrow \infty} \frac{1}{\sqrt[k]{|a_k|}}$$

### 泰勒级数
泰勒定理：设$f(z)$在区域$\sigma$内解析，则在$\sigma$内任意一点$z=\sigma$的邻域$|z-b|< R $（含于$\sigma$内)。则$f(z)$可以展开为泰勒级数：$f(z) = \sum_{k=0}^{\infty} a_k (z-b)^k$
$$ a_k = \frac{1}{k!} f^{k}(b)$$
几个常用的结论：
$$ \frac{1}{1-z} = \sum_{k=0}^{\infty} z^k \quad |z| < 1$$
$$ \frac{1}{1+z} = \sum_{k=0}^{\infty} (-1)^k z^k \quad |z| < 1$$
$$ e^z = \sum_{k=0}^{\infty} \frac{1}{k!} z^k \quad |z| < \infty$$

### 柯西乘积表
对于两个绝对收敛的级数 $\sum_{k=0}^{\infty} a_k$，$\sum_{k=0}^{\infty}b_k$，其积满足柯西乘积表所给定的系数
$$ (\sum_{k=0}^{\infty} a_k)(\sum_{k=0}^{\infty}b_k) = \sum_{k=0}^{\infty} c_k $$
$$c_k = \sum_{n=0}^{k} a_n b_{n-k}$$

### 洛朗级数
形如$$\sum_{k=-\infty}^{\infty}c_k(z-b)^k = ... + c_{-2}(z-b)^{-2} + c_{-1}(z-b)^{-1} + c_0 + c_1(z-b)^1 + c_2(z-b)^2 + ... $$
分为主部和正则部。

**洛朗级数的收敛性定理**：  
令$\xi = \frac{1}{z-b}$，则主部变为$
\sum_{k=0}^{\infty} C_{-k} \xi^k$。设其收敛圆半径为$\frac{1}{\gamma}$，当$|\xi| < \frac{1}{\gamma}$时，$\sum_{k=0}^{\infty}C_{-k} \xi^k$收敛，$\Rightarrow$ 在$|z-b| > \gamma$主部$\sum_{k=-\infty}^{-1} c_k(z-b)^k$收敛，且在更大一点的圆$|z-b| = \gamma' > \gamma$之外一致收敛。
对正则部$\sum_{k=0}^{\infty}c_k(z-b)^k$的收敛半径，在$|z-b| < R$内收敛，在更小一点的闭圆之内$|z-b|=R' < R$之内一致收敛。

**洛朗定理**

在环域$\gamma < |z-b| < R$内解析的函数$f(z)$必可被展开为洛朗级数。
$$f(z) = \sum_{k=-\infty}^{\infty}C_k (z-b)^k$$
其中$$ C_k = \frac{1}{2 \pi i} \oint_l \frac{f(\xi)}{(\xi - b)^{k+1}}$$
$l$为圆周：$|z-b| = \rho$ ($\gamma < \gamma' < \rho < R' < R$)
