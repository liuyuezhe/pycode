import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize

np.random.normal(30)
#y=b0+b1*x+ips
N = 100 #样本数量
x = np.random.normal(0,1,size=N) #随机产生N个01正态分布的x
b0 = -5
b1 = 3
lxy=np.zeros(N)
lxx=np.zeros(N)

sigma = 0.5
sigma = float(sigma)
ips = np.random.normal(0,sigma,N) #随机产生N个0sigma**2正态分布的ips
y = np.zeros(N)


#将变量变换形状
x.reshape([1,N])
ips.reshape([1,N])
y.reshape([1,N])

#合并b0 b1
b=np.hstack((b0,b1))
#合并1矩阵和x
xx=np.vstack((np.ones((1,N)),x))
#计算
y=np.dot(b,xx)+ips

for i in range(N):
    lxy=(x[i]-np.mean(x))*(y[i]-np.mean(y))
    lxx=(x[i]-np.mean(x))**2

b1bar=np.sum(lxy)/np.sum(lxx)
b0bar=np.mean(y)-b1bar*np.mean(x)
epsbar=sum(pow(y-b0bar-b1bar*x,2))/N
print("b0",b0bar)
print("b1",b1bar)
print("eps",epsbar)

#y=b0bar+b1bar*x+epsbar
def Mini(c):
    if c[2]>0:
        return N/2*math.log(2*math.pi*c[2])+sum(pow(y-c[0]-c[1]*x,2))/(2*c[2])
    else:
        return 0
x_0=[-5,3,1]  #初始值
res=minimize(Mini,x_0,method='BFGS')   #BFGS牛顿迭代算法
print('用牛顿迭代算法算出的beta0,beta1,方差分别为：')
print(res.x)

plt.plot(np.arange(-3, 2, 0.01),b0bar+b1bar*np.arange(-3, 2, 0.01))
plt.plot(x,y,'o')
plt.show()
