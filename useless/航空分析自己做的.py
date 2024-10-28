import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(r"class222.xlsx")

# 观察各列数据
print(data)
print('*******************************************************************')
explore = data.describe(percentiles=[], include='all',datetime_is_numeric=True).T #对data数据及基本统计性描述
explore['null'] = len(data) - explore['count'] #该属性缺失的数量
print(explore.columns)#describe函数对data数据所描述的所有统计量
print(explore.head())
print(data.isnull().sum())
print('*******************************************************************')
#在这之后，可以对该数据有一个基本的认识



# 接下来就是处理空缺值
data=data.dropna()#删除缺失值


#由于客户分析，需要了解客户的消费水平，于是对第一第二年消费做简单分析，下面一半是第一年，一半是第二年
#第一年
data=data.sort_values(by='SUM_YR_1')#将data根据SUM_YR_1重新排序
data=data[data['SUM_YR_1']!=0]#去除SUM_YR_1的值为0的行
print(data['SUM_YR_1'])
sy1picture=data.boxplot(column="SUM_YR_1",showmeans=True)#画出箱型图
plt.show()
#计算Q3，Q1,IQR
if data['SUM_YR_1'].count()%2==0 :
    Q3=data['SUM_YR_1'][int(len(data['SUM_YR_1'])/2):].median()
    Q1=data['SUM_YR_1'][:int(len(data['SUM_YR_1'])/2)].median()
elif data['SUM_YR_1'].count()%2 !=0 :
    Q3=data['SUM_YR_1'][int(len(data['SUM_YR_1'])/2-1):].median()
    Q1=data['SUM_YR_1'][:int(len(data['SUM_YR_1'])/2-1)].median()
IQR=round(Q3-Q1,1)
rule=(round(Q3+1.5*IQR,1)<data['SUM_YR_1'])|(round(Q1-1.5*IQR,1)>data['SUM_YR_1'])
index1=np.arange(data['SUM_YR_1'].shape[0])[rule]#index中存放的是异常值的索引
outliers1=data['SUM_YR_1'].iloc[index1]#这是异常值的索引和值
print(outliers1)#我不知道怎么删除这些异常值
print('*******************************************************************')
#第二年
data=data.sort_values(by='SUM_YR_2')#将data根据SUM_YR_1重新排序
data=data[data['SUM_YR_2']!=0]#去除SUM_YR_1的值为0的行
print(data['SUM_YR_2'])
sy2picture=data.boxplot(column="SUM_YR_2",showmeans=True)#画出箱型图
plt.show()
#计算Q3，Q1,IQR
if data['SUM_YR_2'].count()%2==0 :
    Q3=data['SUM_YR_2'][int(len(data['SUM_YR_2'])/2):].median()
    Q1=data['SUM_YR_2'][:int(len(data['SUM_YR_2'])/2)].median()
elif data['SUM_YR_2'].count()%2 !=0 :
    Q3=data['SUM_YR_2'][int(len(data['SUM_YR_2'])/2-1):].median()
    Q1=data['SUM_YR_2'][:int(len(data['SUM_YR_2'])/2-1)].median()
IQR=round(Q3-Q1,1)
rule=(round(Q3+1.5*IQR,1)<data['SUM_YR_2'])|(round(Q1-1.5*IQR,1)>data['SUM_YR_2'])
index1=np.arange(data['SUM_YR_2'].shape[0])[rule]#index中存放的是异常值的索引
outliers2=data['SUM_YR_2'].iloc[index1]#这是异常值的索引和值
print(outliers2)#我不知道怎么删除这些异常值
print('*******************************************************************')

#对总公里数的大致了解
explore1=data['SEG_KM_SUM'].describe()
print(explore1)
sy3picture=data.boxplot(column="SEG_KM_SUM",showmeans=True)#画出箱型图
plt.show()
print('*******************************************************************')
#对平均乘机时间间隔的大致了解
explore2=data['AVG_INTERVAL'].describe()
print(explore2)
sy4picture=data.boxplot(column="AVG_INTERVAL",showmeans=True)#画出箱型图
plt.show()




