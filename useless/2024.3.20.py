import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize
from sympy import symbols,diff,solve
#############################################
#运用回归生成的随机数参数

beta0=-5
beta1=3
sigmal_2=5
k=1000      #生成随机数的个数
print(f'初始参数为beta0={beta0},beta1={beta1},方差为{sigmal_2**2},样本量为{k}')
print()
################################################
x=np.random.normal(size=k)
exps=np.random.normal(0,sigmal_2,k)

#函数的拼接，求出因变量
matrix_1=np.hstack((beta0,beta1))
matrix_2=np.vstack((np.ones((1,k)),x))
A=np.dot(matrix_1,matrix_2)+exps
'''
A=beta0+beta1*x+exps
'''
#求解均值等，计算beta0,beta1,方差
mean_x=np.mean(x)
mean_y=np.mean(A)
x2=np.square(x-mean_x)
beta_1=np.dot(x-mean_x,A-mean_y)/np.sum(x2)
beta_0=mean_y-beta1*mean_x

print(f'beta0估计值为{beta_0}\nbeta1估计值为{beta_1}')
eps_1=sum(pow(A-beta_0-beta_1*x,2))/k
print(f'随机误差的方差估计值为{eps_1}')
print()
####################################################
#定义对数似然函数，用迭代算法进行验证
def Mini(c):
    if c[2]>0:
        return k/2*math.log(2*math.pi*c[2])+sum(pow(A-c[0]-c[1]*x,2))/(2*c[2])
    else:
        return 0
x_0=[-5,3,1]  #设定初始值
res=minimize(Mini,x_0,method='BFGS')   #CG 共轭梯度算法#BFGS牛顿迭代算法
print('用牛顿迭代算法算出的beta0,beta1,方差分别为：')
print(res.x) #输出最小值解
#########################################################
Y=beta_0+beta_1*x
plt.plot(x,Y)
plt.scatter(x,A)
plt.show()