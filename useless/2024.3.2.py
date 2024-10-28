import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
# 从CSV文件加载数据到NumPy数组
data = np.genfromtxt('D:\\办公学习\\内容\\大二下课程\\统计学习课程\\Data\\2.29Advertising.csv', delimiter=',')
# 打印加载后的数组
data=data[1:,1:]
print(data)




# #3d图
#
# # 创建一个新的三维图形
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# # 将四个变量分别赋值给X、Y、Z和C
# X = data[:, 1]
# Y = data[:, 2]
# Z = data[:, 3]
# C = data[:, 4]
# # 绘制散点图
# ax.scatter(X, Y, Z, c=C, cmap='viridis')
# ax.set_xlabel('TV')
# ax.set_ylabel('radio')
# ax.set_zlabel('newspaper')
# ax.set_title('Sales volume')
# # 添加颜色条
# cbar = plt.colorbar(ax.scatter(X, Y, Z, c=C, cmap='viridis'))
# cbar.set_label('sales')
# plt.show()



#九宫格

#创建画布
fig, axes = plt.subplots(nrows=3,ncols=3,figsize=(20,20),dpi=100)
#对角元素显示分布
for i in range(3):
    axes[i][i].hist(data[:, i],bins=50,edgecolor='black')
#上三角元素显示相关系数
for i in range(2):
    for j in range(2):
        if i>j:
            continue
        axes[i][j+1].text(0.5, 0.5,np.around(np.corrcoef(data[:,i],data[:,j+1])[0,1],4), ha='center', fontsize=20)
        axes[i][j+1].axis('off')
#下三角显示相关分布图
for i in range(2):
    for j in range(2):
        if i<j:
            continue
        axes[i+1][j].scatter(data[:,i+1],data[:,j])
plt.show()


