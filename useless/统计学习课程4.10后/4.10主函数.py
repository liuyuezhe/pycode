import numpy as np
import matplotlib.pyplot as plt
import 定义变量 as den
import 变量操作 as es
#y=b0+b1*x+ips


##################################################
np.random.seed(30)
n = 1000 #变量数量
k = 100 #重复次数
b0 = 3 #截距
b1 = 5 #斜率
mux = 0 #x均值
sigmax = 1 #x标准差
##################################################


#误差标准差
##################################################
# sigma = np.linspace(1,5,k)
sigma = np.full(k,2)
##################################################


#定义所需变量
##################################################
ihb1 = np.zeros(k)
ihb0 = np.zeros(k)
ihsigmafang = np.zeros(k)
isebeta1 = np.zeros(k)
isebeta0 = np.zeros(k)
uihb0 = np.zeros(k)
dihb0 = np.zeros(k)
uihb1 = np.zeros(k)
dihb1 = np.zeros(k)
##################################################


#循环k次，得到k和h0h1估计值
##################################################
for i in range(0,k):
    x,y = den.makenormalxy(b0, b1, mux, sigmax, sigma[i], n)
    hb1, hb0, hsigmafang, sebeta1, sebeta0 = es.est(x,y,n)
    ihb1[i] = hb1
    ihb0[i] = hb0
    ihsigmafang[i] = hsigmafang
    isebeta1[i] = sebeta1
    isebeta0[i] = sebeta0
##################################################


#b0b1的置信区间
##################################################
ihb1std = np.std(ihb1)
ihb0std = np.std(ihb0)
a = 2
for j in range(0,k):
    uihb0[j] = ihb0[j]+a*ihb0std
    dihb0[j] = ihb0[j]-a*ihb0std
    uihb1[j] = ihb1[j]+a*ihb1std
    dihb1[j] = ihb1[j]-a*ihb1std
##################################################


#画图
##################################################
plt.figure(figsize=(13,8))

plt.subplot(4,1,1)
plt.plot(ihb1)
plt.axhline(b1)
for i in range(k):
    if dihb1[i] <= b1 <= uihb1[i]:
        plt.vlines(i,dihb1[i],uihb1[i],linestyles ='-',colors='red')
    else:
        plt.vlines(i,dihb1[i],uihb1[i],linestyles ='-',colors='black')
    plt.plot(i,dihb1[i],'o',alpha=0.1)
    plt.plot(i,uihb1[i], 'o',alpha=0.1)
plt.title ('ihb1')

plt.subplot(4,1,2)
plt.plot(ihb0)
plt.axhline(b0)
success = 0
for i in range(k):
    if dihb0[i] <= b0 <= uihb0[i]:
        plt.vlines(i, dihb0[i], uihb0[i], linestyles='-', colors='red')
        success = success+1
    else:
        plt.vlines(i, dihb0[i], uihb0[i], linestyles='-', colors='black')
    plt.plot(i,dihb0[i],'o',alpha=0.1)
    plt.plot(i,uihb0[i], 'o',alpha=0.1)

print("在置信区间内的概率为：",success/k)

plt.title ('ihb0')

plt.subplot(4,1,3)
plt.plot(ihsigmafang)
plt.axhline(4)
plt.title ('ihsigmafang')

plt.subplot(4,1,4)
plt.plot(ihb1)
plt.plot(ihb0)
plt.plot(ihsigmafang)
plt.axhline(3)
plt.axhline(4)
plt.axhline(5)
plt.title ('combined')

plt.show()

