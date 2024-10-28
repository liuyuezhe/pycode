import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

np.random.seed(110)
#定义x
##########################################################
mux = 0
sigmax = 1
n = 1500
x = np.random.normal(mux, sigmax**2, size=n)
##########################################################

#定义y
##########################################################
b0 = 3
b1 = 5
p = 1/(1+np.exp(-b0-b1*x))
y = np.random.binomial(1,p)
##########################################################

#区分训练集和测试集
##########################################################
xtest = x[1000:n]
ytest = y[1000:n]
x = x[:1000]
y = y[:1000]
n = 1000
##########################################################

#梯度下降实现
##########################################################
hb0 = 1  # 定义迭代初始点
hb1 = 1
loss_list = []
learn_rate = 2
w = np.array([hb1,hb0])
x = np.vstack((x,np.ones(n)))
x = x.T

for i in range(300):
    g_x = np.dot(x,w)
    h_x = 1/(1+np.exp(-g_x)) #Sigmoid函数

    # 计算损失函数 Cost Function 的关于b0 b1的导数
    loss = np.log(h_x) * y + (1-y) * np.log(1-h_x)
    loss = -np.sum(loss) / n
    loss_list.append(loss)

    # 梯度下降函数更新W权重
    dW = np.dot(x.T,h_x - y) / n
    w = w-learn_rate * dW

##########################################################

#根据增大判断值
##########################################################

hb0 = w[1]
hb1 = w[0]
tpr = []
fpr = []
hp = 1/(1+np.exp(-hb0-hb1*xtest)) #y_hat

for j in np.arange(0,1,0.01):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    hy = np.zeros(len(hp))
    hy = hy.astype(int)
    for i in range(len(hp)):
        if j < hp[i]:
            hy[i] = 1
        else:
            hy[i] = 0

    for i in range(len(hp)):
         if hy[i] == 1 and ytest[i] == 1:
            tp = tp+1
         elif hy[i] == 0 and ytest[i] == 1:
            fn = fn+1
         elif hy[i] == 0 and ytest[i] == 0:
            tn = tn+1
         elif hy[i] == 1 and ytest[i] == 0:
            fp = fp+1

    tpr.append(tp/(tp+fn))
    fpr.append(fp/(fp+tn))

print(len(tpr),len(fpr))

plt.plot(fpr,tpr)
plt.show()
