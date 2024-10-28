import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import 定义变量 as den
import 变量操作 as es

# 从CSV文件加载数据到NumPy数组
data = np.genfromtxt('D:\\办公学习\\内容\\大二下课程\\统计学习课程\\Data\\2.29Advertising.csv', delimiter=',')
# 打印加载后的数组
data=data[1:,1:]

s = len(data[0,:])
c = np.eye(s)


for i in range(s):
    for j in range(i+1,s,1):
        c[i,j] = (np.corrcoef(data[:,i],data[:,j]))[0,1]

print(c)

mask = np.zeros_like(c)
mask[np.tril_indices_from(mask,k=-1)] = True
plt.subplots(figsize = (7,7))
sns.heatmap(c,annot = True,vmin = 0,vmax = 1,square = True,cmap = "Reds",mask = mask)
plt.show()