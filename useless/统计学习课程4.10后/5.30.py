import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0,1,size=(2,100))
beta = np.array(object=[2,3,4])

p = beta[0]+beta[1:3]@x
y = np.exp(p)/(1+np.exp(p))
y = np.random.binomial(1,y)


fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(len(y)):
    if y[i] == 0:
        ax.scatter(x[0,i],x[1,i],y[i],color='r')
    else:
        ax.scatter(x[0,i],x[1,i],y[i],color='b')

x0min, x0max = x[0].min(), x[0].max()
x1min, x1max = x[1].min(), x[1].max()
xx0, xx1 = np.meshgrid(np.linspace(x0min, x0max, 100), np.linspace(x1min, x1max, 100))
x3 = (-beta[0] - beta[1] * xx0 - beta[2] * xx1)
print(x3.shape)
ax.plot_surface(xx0, xx1, x3, alpha=0.5, color='green')

plt.show()