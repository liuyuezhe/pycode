import numpy as np

def makenormalxy(b0,b1,mux,sigmax,sigma,n):
    np.random.normal(30)
    x = np.random.normal(mux, sigmax**2, size=n)  # 随机产生N个01正态分布的x
    sigma = float(sigma)
    ips = np.random.normal(0, sigma**2, size=n)  # 随机产生N个0sigma**2正态分布的ips
    y = b0 + b1 * x + ips
    return x,y

def makenormalx(mux,sigmax,n):
    np.random.normal(30)
    x = np.random.normal(mux, sigmax**2, size=n)
    return x

