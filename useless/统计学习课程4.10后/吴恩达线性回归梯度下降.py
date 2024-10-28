import numpy as np
import matplotlib.pyplot as plt
import 定义变量 as de

##生成数据
np.random.seed(30)
n = 1000 #变量数量
B0 = 3 #截距
B1 = 5 #斜率
mux = 4 #x均值
sigmax = 2 #x标准差
sigma = 5
x,y = de.makexy(B0, B1, mux, sigmax, sigma, n)

##定义hx假设函数
def h(b0,b1,x):
    return b0 + b1 * x

##定义j损失函数  J(b0,b1) = 1/2n * sum(b0+b1*xi-yi)^2
def j(b0,b1,x,y,n):
    fval = 0
    for i in range(n):
        fval = fval + (h(b0,b1,x[i])-y[i])**2
    fval = fval*(1/(2*n))
    return fval


##设置下降起始点位置
b0 = 0
b1 = 0
##设置步长
a = 0.01
##设置停止条件变量
s = 1
##设置临时变量
temp0 = 0
temp1 = 0
b00 = 0
b10 = 0
m = 0


##梯度下降算法
while s > 0.0001:
    temp0 = b0 - a * (1 / n) * np.sum(h(b0,b1,x) - y)
    temp1 = b1 - a * (1 / n) * np.sum((h(b0,b1,x) - y) * x)
    b0 = temp0
    b1 = temp1
    s = abs(j(b0,b1,x,y,n) - j(b00,b10,x,y,n))
    b00 = b0
    b10 = b1
    m = m+1


print('迭代次数为：',m)
plt.plot(x,y,'o')
plt.plot(np.linspace(min(x),max(x),100),b0+np.linspace(min(x),max(x),100)*b1)
plt.show()