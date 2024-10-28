import numpy as np
from pandas import read_csv
from sklearn import svm
from sklearn import datasets
import matplotlib.pyplot as plt 

iris = datasets.load_iris()

x = iris.data[:100,:2]
y = iris.target[:100]

clf = svm.SVC()
clf.fit(x,y)

plt.figure()
ax = plt.subplot(121,projection = '3d')
ax.scatter(x[:,0],x[:,1],y,'o')

bx = plt.subplot(122)
bx.scatter(x[:,0],x[:,1],c=y,s=30,cmap=plt.cm.Paired)

bx = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 创造网格来评估模型
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# 绘制决策边界和边际
bx.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,linestyles=['--', '-', '--'])
plt.show()

