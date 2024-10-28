import numpy as np
import matplotlib.pyplot as plt
import math


np.random.seed(30)
N = 100 #样本数量
x = np.random.normal(0,1,N) #随机产生N个01正态分布的x
b0 = -5
b1 = 3

sigma = 2
sigma = float(sigma)
ips = np.random.normal(0,sigma**2,N) #随机产生N个01正态分布的ips
y = np.zeros(N)

# #用for循环
# for i in range(100):
#     # y[i] = b0+b1*(math.exp(x[i]))+ips[i]
#     y[i] = b0+b1*(x[i])+ips[i]
#
# plt.plot(x,y,'o')
# plt.show()


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

plt.plot(x,y,'o')
plt.show()


# #第二种方式取b和x
# b=np.zeros((1,2))
# b[:,0]=b0
# b[:,1]=b1
#
# xx=np.zeros((2,N))
# xx[0,:]=np.ones((1,N))
# xx[1,:]=x
# #计算
# y=np.dot(b,xx)+ips
#
# plt.plot(x,y.T,'o')
# plt.show()



