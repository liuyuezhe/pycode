import numpy as np
import matplotlib.pyplot as plt

# print(np.random.normal(size=50))#01正态分布
# print(np.random.rand(3,4)) # 01均匀分布
# print(np.random.exponential(size=50))#指数
# print(np.random.poisson(size=50))#泊松
# print(np.random.f(0.98, 15.43, size=50))#f
# print(np.random.gamma(3,20,size=50))#gamma

# x=[3,4,5]
# y=[4,9,7]
# print(x+y)
#
# x=np.array([3,4,5])
# y=np.array([4,9,7])
# print(x+y)

# x=np.array([[1,2],[3,4]])
# print(x)
# print(x.ndim)
# print(x.dtype)

# print(np.array([[1,2],[3.0,4]]).dtype)
# print(np.array([[1,2],[3,4]],float).dtype)

# x=np.array([[1,2],[3,4]])
# print(x.shape)

# x=np.array([1,2,3,4])
# print(x.sum())
# print(np.sum(x))

# x=np.array([1,2,3,4,5,6])
# print('beginning x:\n',x)
# x_reshape=x.reshape((2,3))
# print('reshaped x:\n',x_reshape)
# print(x_reshape[0,0])
# print(x_reshape[1,2])
# x_reshape[0,0]=5
# print(x)
# print(x_reshape)
# print(x_reshape.shape,x_reshape.ndim,x_reshape.T)
# print(np.sqrt(x))
# print(x**2)
# print(x**0.5)

# x=np.random.normal(size=50)
# y=x+np.random.normal(loc=50,scale=1,size=50)
# print(x)
# print(y)
# print(np.corrcoef(x,y))

# print(np.random.normal(scale=5, size=2))
# print(np.random.normal(scale=5, size=2))

rng = np.random.default_rng(1303)
print(rng.normal(scale=5, size=2))
rng2 = np.random.default_rng(13)
print(rng2.normal(scale=5, size=2))

# rng=np.random.default_rng(3)
# y=rng.standard_normal(10)
# print(np.mean(y), y.mean())
# print(np.var(y), y.var(), np.mean((y - y.mean())**2))
# print(np.sqrt(np.var(y)), np.std(y))
# x=rng.standard_normal((10, 3))
# print(x)
# print(x.mean(axis=0))
# print(x.mean(0))









