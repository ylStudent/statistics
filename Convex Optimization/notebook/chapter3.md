## 凸函数
### 3.1 基本性质和例子
### 3.1.1 定义
函数$f:R^n ->R$是凸的，如果$dom f$是凸集，且对于任意$x, y \in domf$和任意$0 <= \theta <=1$，有：
$$ f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta) f(y) $$
函数是凸的，当且仅当其在于其定义域相交的任意直线上都是凸的。

换言之，函数$f$是凸的，当且仅当对于任意$x \in domf$ 和任意向量$v$，函数$g(t) = f(x + tv)$是凸的（其定义域为$\{t| x + tv \in dom f\}$。(证明后续补)

**一阶条件**

假设$f$可微（即其梯度$\bigtriangledown f$在开集$domf$内处处促成你在），则函数$f$是凸函数的充要条件是$domf$是凸集且对于任意$x,y \in domf $下式成立：
$$ f(y) \geq f(x) + \bigtriangledown f(x)^T(y-x)$$

**二阶条件**

假设函数$f$二阶可微，即对于开集$domf$内的任意一点，它的Hessian矩阵或者二阶导数$\bigtriangledown^2f$存在，则函数f是凸函数的充要条件是，其Hessian矩阵式半正定矩阵：即对于所有的$x \in domf$，有：
$$ \bigtriangledown^2 f(x) \geq 0 $$

**例子**：

指数函数：对于$a \in R$，函数$e^{ax}$在$R$上是凸的。  

幂函数：函数$f(x) = x^a$在$R_{++}$上当$a \leq 0$时对数-凸函数，当$a \geq 0$时对数-凹函数。

指数函数：函数$f(x) = e^{ax}$既是对数-凸函数，也是对数-凹函数。

Guass概率密度函数的累计分布函数
$$ \Phi(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{\frac{-u^2}{2}}du $$
是对数凹函数。

行列式 $det X$ 在$S^n_{++}$上是对数-凹函数。

行列式与迹之比。 $det X / trX$在$S^n_{++}$上是对数-凹函数。





