import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import math


def newtonmethod(func, x0, tol=0.000001, maxiter=10000):

    x = sp.Symbol('x')
    f = sp.sympify(func)
    df = sp.diff(f, x)

    iternum = 0
    step=0.5
    i=0
    fval=[]
    dfval=[]
    x1=[]
    x0=float(x0)

    while True:
        fval.append(f.subs(x, x0))
        dfval.append(df.subs(x, x0))
        x1.append(x0)
        if abs(fval[i]) < tol or iternum >= maxiter:
            break
        # x0 = x0 - fval[i]/dfval[i] #不带步长
        x0 = x0 - step*(fval[i]/dfval[i]) #带步长
        iternum += 1
        i += 1

    if iternum >= maxiter:
        print("达到最大迭代次数")
    else:
        print(" 根的值为:", x0,"\n","函数值为：",fval[-1],"\n","迭代次数为：",iternum)

    sp.plot(f,(x))

    plt.figure(figsize=(10,6),layout='constrained')
    x = np.linspace(float(x1[-1]-0.2), x1[0], 10000)
    for j in range(iternum+1):
        if j==0:
            plt.plot(x, eval(func),linewidth=4)
        xk = np.linspace(float(x1[j]-0.5), x1[0], 10000)
        plt.plot(xk,(dfval[j] * (xk - x1[j]) + fval[j]),linewidth=0.5)
        plt.plot(x1[j],fval[j],'o')

    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.grid(True)
    plt.show()


func = "x**2-20"
x0 = 3
newtonmethod(func, x0)




