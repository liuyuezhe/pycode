import numpy as np
import matplotlib.pyplot as plt
np.random.normal(30)
#y=b0+b1*x+ips

#data
N = 1000 #样本数量
x = np.random.normal(0,1,size=N) #随机产生N个01正态分布的x
b0 = 3
b1 = 5
sigma = 2
sigma = float(sigma)
ips = np.random.normal(0,sigma**2,size=N) #随机产生N个0sigma**2正态分布的ips
y=b0+b1*x+ips

#估计
hb1 = np.sum((x-np.mean(x))*(y-np.mean(y)))/np.sum((x-np.mean(x))**2)
hb0 = np.mean(y)-hb1*np.mean(x)
hsigma = np.sqrt(((np.sum(y-np.mean(y)))**2)*(1/ N))
sebeta0 = hsigma**2 * (1/N+np.mean(x)**2 * np.sum((x-np.mean(x))*(x-np.mean(x))))
sebeta1 = hsigma**2 / (np.sum((x-np.mean(x))**2))
uhb1 = hb1+2*sebeta1
dhb1 = hb1-2*sebeta1
print(hb1,hb0)
print(hsigma)

#画图
plt.plot(x,y,'o')
plt.plot(np.arange(min(x)-0.5, max(x)+0.5, 0.001),hb0+hb1*np.arange(min(x)-0.5, max(x)+0.5, 0.001),color='deepskyblue')
plt.plot(np.arange(min(x)-0.5, max(x)+0.5, 0.001),b0+b1*np.arange(min(x)-0.5, max(x)+0.5, 0.001),color='black')
plt.plot(np.arange(min(x)-0.5, max(x)+0.5, 0.001),hb0+uhb1*np.arange(min(x)-0.5, max(x)+0.5, 0.001),color='green')
plt.plot(np.arange(min(x)-0.5, max(x)+0.5, 0.001),hb0+dhb1*np.arange(min(x)-0.5, max(x)+0.5, 0.001),color='yellow')

plt.show()