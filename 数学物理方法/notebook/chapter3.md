## 复变函数级数理论
### 1. 复变项级数
形如$f_1 + f_2 + ... + f_k = \sum_{k=1}^{\infty}f_k$的级数（其中$f_k = u_k + iv_k$）称为复级数。
$$ \sum_{k=1}^{\infty} f_k = \sum_{k=1}{\infty}u_k + i\sum_{k=1}^{\infty}v_k $$

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

比值判别法（达朗贝尔判别法）:  
若$\sum_{k=1}^{f_k}$的通项$f_k(k=1,2...)$满足：$$\lim_{k \rightarrow \infty} \frac{f_{k+1}}{f_k} = l$$  
若 $l < 1$，则$\sum_{k=1}^{f_k}$绝对收敛； 若 $l > 1$，则$\sum_{k=1}^{f_k}$发散； 当 $l = 1$，则$\sum_{k=1}^{f_k}$的敛散性无法判断。

高斯判别法
对于$ \sum_{k=1}^{\infty} f_k $，若$\frac{f_k}{f_{k+1}} = 1 + \frac{\mu}{k} + O(\frac{1}{k^{\lambda}}), \lambda > 0$

若$Re\ \mu > 1$，则$\sum_{k=1}^{\infty}f_k$绝对收敛

若$Re\ \mu <= 1$，则$\sum_{k=1}^{\infty}f_k$发散


















