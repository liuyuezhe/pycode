import numpy as np
import matplotlib.pyplot as plt

np.random.seed(56)
p = 5
n = 1000
sigma = 1

mu = 0
x = np.random.normal(0,1,size=(p+1,n))

# mean = [0,0,0,0,0,0]
# cov = [[1,0.5,0,0,0,0],
#        [0.5,1,0.5,0,0,0],
#        [0,0.5,1,0.5,0,0],
#        [0,0,0.5,1,0.5,0],
#        [0,0,0,0.5,1,0.5],
#        [0,0,0,0,0.5,1]]
# x = np.random.multivariate_normal(mean, cov, size=(n))
# x = x.T


x[0] = 1
beta = np.random.randint(1,10,(p+1,1))
eps = np.random.normal(0,sigma**2,size=(1,n))
y = beta.T@x + eps

print('原beta为：',beta.T)
beta0 = (np.linalg.inv(x@x.T)@(x))@y.T
print('估计beta为：',beta0.T)

m = np.arange(1,10)
plt.plot(beta,beta0,'o')
plt.plot(m,m)
plt.show()