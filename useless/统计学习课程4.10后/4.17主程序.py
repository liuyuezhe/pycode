import numpy as np
import matplotlib.pyplot as plt
import 定义变量 as den
import 变量操作 as es
#y=b0+b1*x+ips


##################################################
# np.random.seed(30)
n = 100 #变量数量
k = 100 #重复次数
b0 = 3 #截距
b1 = 5 #斜率
mux = 0 #x均值
sigmax = 1 #x标准差
##################################################


#误差标准差
##################################################
sigma = 2
#sigma = np.linspace(1,5,k)
##################################################


#生成xy数据并估计
##################################################
x,y = den.makenormalxy(b0, b1, mux, sigmax, sigma, n)
hb1, hb0, hsigmafang, sebeta1, sebeta0 = es.est(x,y,n)
##################################################


#求rss
##################################################
rss = np.sum((y-hb0-hb1*x)**2)
##################################################

#求tss
##################################################
tss = np.sum((y-np.mean(y))**2)
##################################################


#求rse
##################################################
rse = np.sqrt(rss/(n-2))
##################################################


#求r^2
##################################################
rfang = 1-rss/tss
##################################################


#计算置信区间
##################################################
a = 2
uhb1,dhb1,uhb0,dhb0 = es.confidence(hb1,hb0,sebeta1,sebeta0,a)
##################################################


#画图
##################################################
s = "r^2 value:",float('%.3f'%rfang)
fig, ax = plt.subplots()
ax.plot(x,y,'o')
ax.plot(np.linspace(min(x),max(x),100),hb0+np.linspace(min(x),max(x),100)*hb1)
ax.plot(np.linspace(min(x),max(x),100),dhb0+np.linspace(min(x),max(x),100)*dhb1)
ax.plot(np.linspace(min(x),max(x),100),uhb0+np.linspace(min(x),max(x),100)*uhb1)
ax.text(max(x)-5,max(y)+5,s, fontsize=15, color='green')
ax.fill_between(np.linspace(min(x),max(x),100), dhb0+np.linspace(min(x),max(x),100)*dhb1, uhb0+np.linspace(min(x),max(x),100)*uhb1, alpha=0.2)
plt.show()
##################################################
