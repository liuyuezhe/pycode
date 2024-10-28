import numpy as np

m = 100
alpha = np.random.normal(0,1,size=[m,1])
# alpha[5] = 1
# alpha[8] = 2


index = np.ones([m,1])
timesnum = 0
alphasum = 0
alphasumnum = 0

if(alphasum<=0):
    alphasumnum = alphasumnum+1
    while(np.sum(index)!=0):
        res = np.random.uniform(-1,1,[2,1])
        i = np.random.randint(0,m)
        j = np.random.randint(0,m)
        iv = np.array([i,j])
        alpha[iv] = res.reshape(2,1)
        index[iv] = np.zeros([2,1])
        timesnum = timesnum+1
    alphasum = np.sum(alpha)
    print(alpha)
    print(alphasum)

print(alphasumnum)