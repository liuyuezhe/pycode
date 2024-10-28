import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import math
###############################################################
#定义函数及其导数
x=sp.symbols('x')
string=input('请输入需要进行牛顿迭代求解的函数：')
expr=sp.parse_expr(string)
f=sp.lambdify(x,expr)    #将字符串形式改为
sp_df=sp.diff(expr,x)
df=sp.lambdify(x,sp_df)
print('如果想实现一般牛顿迭代算法并绘制图像请输入Newtonplot()\n'
      '如果想实现带步长的牛顿迭代算法请输入Newton()')
###################################################################
#不带步长的一般牛顿算法的的绘图和实现
def Newtonplot():
    dot_0=eval(input('请输入一般牛顿迭代的初始点:'))
    Min=eval(input('请输入绘图区间的下界：'))
    Max=eval(input('请输入绘图区间的上界：'))
    temp_int=0
    space=abs(f(dot_0))
    x_1=np.linspace(Min,Max,50*(Max-Min))
    y_0=np.linspace(Min,Max,50*(Max-Min))
    y_1=np.linspace(Min,Max,50*(Max-Min))
    for i in range(50*(Max-Min)):
        y_0[i]=f(x_1[i])
    plt.plot(x_1,y_0)
    while space>0.1:
        temp_int+=1
        plt.scatter(dot_0,f(dot_0))
        for i in range(50*(Max-Min)):
            y_1[i]=f(dot_0)+df(dot_0)*(x_1[i]-dot_0)
        plt.plot(x_1,y_1,'--',linewidth=1.5)
        dot_0=-f(dot_0)/df(dot_0)+dot_0
        space=abs(f(dot_0))
    plt.axhline(y=0,linewidth=1)
    print(f'迭代次数为{temp_int}')
    print(f'牛顿迭代法找到的根为{dot_0}')
    plt.show()
    return 0


###########################################################
#带步长的牛顿算法的实现
def Newton():
    dot_0=eval(input('请输入一般牛顿迭代的初始点:'))
    gap=eval(input('请输入牛顿迭代的步长：'))
    temp_int=0
    space=abs(f(dot_0))
    while space>0.1 :
        plt.scatter(dot_0,f(dot_0))
        dot_0=dot_0-df(dot_0)*gap
        space=abs(f(dot_0))
        temp_int+=1
    print(f'迭代次数为{temp_int}')
    print(f'牛顿迭代法找到的根为{dot_0}')
    return 0
