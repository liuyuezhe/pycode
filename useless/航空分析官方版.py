import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_excel(r"class222.xlsx")

# # 观察各列数据
# print(data.head())#head就是拿前五行做一个例子，并不影响整体的值
# print(data.columns)
# explore = data.describe(percentiles=[], include='all',datetime_is_numeric=True).T #对data数据及基本统计性描述
# explore['null'] = len(data) - explore['count'] #该属性缺失的数量
# print(explore.columns)#describe函数对data数据所描述的所有统计量
# print(explore.head())
# print(data.isnull().sum())

# 去除脏数据并只保留需要使用得字段
data_cleaned=[data["SUM_YR_1"].notnull()&data["SUM_YR_2"].notnull()]
print(data_cleaned)
#目前data_cleaned该变量中存的是sumyr1sumyr2两个都不为空的true和存在空为f的一个bool变量
flag1=data["SUM_YR_1"]!=0
flag2=data["SUM_YR_2"]!=0
flag3=(data["SEG_KM_SUM"]==0)&(data["avg_discount"]==0)
print(flag3)
data_cleaned = data_cleaned[flag1|flag2|flag3]
print(data_cleaned)
data_cleaned = data_cleaned.reset_index(drop=True)
data_sepc = data_cleaned[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]

# # 将数据字段转换成LRFMC
# data_sepc['LOAD_TIME'] = pd.to_datetime(data_sepc['LOAD_TIME'])
# data_sepc['FFP_DATE'] = pd.to_datetime(data_sepc['FFP_DATE'])
# data_LRFMC = pd.DataFrame()
# data_LRFMC['L'] = ((data_sepc['LOAD_TIME'] - data_sepc['FFP_DATE']) / np.timedelta64(1, 'D')) / 30
# data_LRFMC['R'] = data_sepc['LAST_TO_END']
# data_LRFMC['F'] = data_sepc['FLIGHT_COUNT']
# data_LRFMC['M'] = data_sepc['SEG_KM_SUM']
# data_LRFMC['C'] = data_sepc['avg_discount']

# # 对LRFMC进行规格化处理
# data_std_scale = (data_LRFMC - data_LRFMC.mean(axis=0)) / (data_LRFMC.std(axis=0))
# data_std_scale.columns = ['Z'+i for i in data_std_scale.columns]
# print(data_std_scale.head())