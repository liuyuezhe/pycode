# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # import numpy as np
# #
# #
# # class BankerAlgorithm():
# #     def __init__(self, available, max, allocation, need):
# #         """
# #         初始化参数
# #         :param available: 可利用资源向量
# #         :param max: 最大需求矩阵
# #         :param allocation: 分配矩阵
# #         :param need: 需求矩阵
# #         """
# #         self.available = available
# #         self.max = max
# #         self.allocation = allocation
# #         self.need = need
# #
# #     def Request(self, P, request):
# #         """
# #         请求资源
# #         :param P: 进程号，从0开始
# #         :param request: 所请求的资源向量
# #         :return: 若成功，打印安全序列，进行分配；否则，拒绝请求。
# #         """
# #         # 判断请求向量是否小于需求向量
# #         length = len(request)
# #         i = 0
# #         for i in range(length):
# #             if request[i] > self.need[P][i]:
# #                 break
# #         if i != len(request) - 1:
# #             print("进程{0}所需资源超过它所宣布的最大值".format(P))
# #             return
# #
# #         # 判断请求向量是否小于可用资源向量
# #         j = 0
# #         for j in range(length):
# #             if request[i] > self.available[i]:
# #                 break
# #         if j != length - 1:
# #             print("尚未足够的资源供{}使用", P)
# #             return
# #
# #         # 试分配
# #         avi_temp = self.available
# #         all_temp = self.allocation
# #         need_temp = self.need
# #
# #         for k in range(length):
# #             avi_temp[k] = avi_temp[k] - request[k]
# #             all_temp[P][k] = all_temp[P][k] + request[k]
# #             need_temp[P][k] = need_temp[P][k] - request[k]
# #
# #         # 执行安全性算法，若存在安全序列，执行分配
# #         if self.Security():
# #             self.need = need_temp
# #             self.allocation = all_temp
# #             self.available = avi_temp
# #             print("请求成功！各数据结构修改为\nNeed={0}\nAllocation={1}\nAvailable{2}\n".format(self.need, self.allocation, self.available))
# #
# #         else:
# #             print("如此分配会导致系统处于不安全状态，拒绝本次分配")
# #             return
# #
# #     def Security(self):
# #         """
# #         安全性算法，检验试分配后系统是否处于安全状态。
# #         :return: 若分配后系统处于安全状态，打印安全序列并返回True；否则返回False
# #         """
# #         work = self.available
# #         finish = [False for i in range(self.need.shape[0])]
# #         pro_number = self.need.shape[0]
# #         pro_list = [i for i in range(pro_number)]
# #         length = self.need.shape[1]
# #         secureSeq = ""
# #
# #         # 寻找安全序列
# #         for k in range(pro_number):
# #             for i in pro_list:
# #                 flag = 1
# #                 for j in range(length):
# #                     if self.need[i][j] > work[j]:
# #                         flag = 0
# #                         break
# #
# #                 if flag and finish[i] is False:
# #                     work += self.allocation[i]
# #                     finish[i] = True
# #                     secureSeq += str(i) + "->"
# #                     pro_list.remove(i)
# #                     break
# #
# #         for i in range(len(finish)):
# #             if finish[i] is not True:
# #                 return False
# #         print("存在安全序列为{0}".format(secureSeq.strip("->")))
# #         return True
# #
# #
# # if __name__ == "__main__":
# #     avi = np.array([3, 3, 2])  # 可利用资源向量
# #
# #     need = np.array([[7, 4, 3],
# #                      [1, 2, 2],
# #                      [6, 0, 0],
# #                      [0, 1, 1],
# #                      [4, 3, 1]])  # 需求矩阵
# #     all = np.array([[0, 1, 0],
# #                      [2, 0, 0],
# #                      [3, 0, 2],
# #                      [2, 1, 1],
# #                      [0, 0, 2]])  # 分配矩阵
# #     max = np.array([[7, 5, 3],
# #                     [3, 2, 2],
# #                     [9, 0, 2],
# #                     [2, 2, 2],
# #                     [4, 3, 3]])  # 最大需求矩阵
# #     Test = BankerAlgorithm(avi, max, all, need)
# #     Test.Request(1, np.array([1, 0, 2]))
#
#
# # 将逻辑地址转换为物理地址
# # 页面大小为1024字节
# # import math
# # d={}
# # dd={}
# # n=eval(input("请输入页表长度"))
# # yehao=[]
# # for j in range(n):
# #     yehao.append(j)
# # for i in range(n):
# #     print("页号为",i)
# #     kuaihao=eval(input("请输入页号对应块号"))
# #     wulidizhi=str(input("请输入块号存储的物理地址"))
# #     d[yehao[i]]=kuaihao
# #     dd[kuaihao]=wulidizhi
# # while True:
# #     luojidizhi=eval(input("请输入逻辑地址"))
# #     yehao1=math.floor(luojidizhi/1024)
# #     if yehao1 in d.keys():
# #         print("逻辑地址对应的块号为：{},物理地址为:{}".format(d.get(yehao1),dd.get(d.get(yehao1))))
# #     else:
# #         print("超过页表长度，越界中断")
#
# # import numpy as np
# # arr1=np.array([1,2,3])
# # print(arr1)
# # arr2=np.array([[1,2,3],[4,5,6]])
# # print(arr2)
# # list_1=[1,1,1]
# # list_2=[6,6,6]
# # arr3=np.array([[list_1,list_2],[list_1,list_2]])
# # print(arr3)
# # import numpy as np
# # arr1=np.zeros((2,3))
# # print(arr1)
# # arr2=np.ones((2,3))
# # print(arr2)
# # arr3=np.empty((4,3))
# # print(arr3)
# # arr4=np.arange(1,30,5)
# # print(arr4)
# # arr44=arr4.reshape((2,3))
# # print(arr44)
# # arr5=np.arange(1,7)
# # print(arr5)
# # print(arr5[3])
# # arr6=np.arange(7,15).reshape((2,4))
# # print(arr6)
# # print(arr6[1])
# # print(arr6[1,2])
# # import numpy as np
# # arr1=np.arange(1,10)
# # print(arr1[[2,5,8]])
# # arr2=np.arange(0,20).reshape((4,5))
# # print(arr2)
# # print(arr2[[0,2],[3,4]])
# # print(arr2>6)
# # print(arr2[arr2>10].reshape((3,3)))
# # import numpy as np
# # # arr1=np.array([10,20,30,40,50,60])
# # # print(arr1[:3])
# # # print(arr1[:-1])
# # # print(arr1[:])
# # # print(arr1[::2])
# # # arr2 = np.arange(0, 20).reshape((4, 5))
# # # print(arr2[:2,0])
# # arr3 = np.arange(0,9).reshape(3,3)
# # arr4 = np.arange(0,9).reshape(3,3)
# # print(arr3)
# # print(arr4)
# # arr5=arr3+arr4
# # print(arr5)
# # import numpy as np
# # arr1=np.array([[1],[2],[3]])
# # arr2=np.array([1,2,3])
# # print(arr1+arr2)
# # import numpy as np
# # arr1=np.array([[6,6,50],[7,23,6],[87,54,32]])
# # print(np.all(arr1>4))
# # print(np.any(arr1>4))
# # print(np.unique(arr1))
# # import numpy as np
# # arr=np.arange(24).reshape(2,3,4)
# # arr1=arr.swapaxes(1,2)
# # print(arr)
# # newarr=arr.transpose((1,2,0))
# # print(newarr)
# # import pandas as pd
# # ok1=pd.Series(['apple','banana','pear'],index=['z1','z2','z3'],name='666')
# # print(ok1)
# # import pandas as pd
# # from datetime import datetime
# # dateindex=pd.to_datetime(['20230301','20230311','20230315'])
# # print(dateindex)
# # dateser=pd.Series(['no1','no2','no3'],index=dateindex,name='omg')
# # print(dateser)
# # import pandas as pd
# # import numpy as np
# # arr=np.array([['a','b','c'],['d','e','f']])
# # arr1=pd.DataFrame(arr,index=['r1','r2'],columns=['c1','c2','c3'])
# # print(arr1)
# # print(arr1.at['r1','c3'])
# # print(arr1.iat[1,1])
# import pandas as pd
# import numpy as np
# # df=pd.DataFrame({'cola':[23,69,55,14],'colb':[75,14,0,33],'colc':[48,15,36,56],'cold':[54,21,49,50]},index=['a','b','c','d'])
# # print(df)
# # print(df.max())
# # print(df.idxmax())
# df=pd.DataFrame({'object':['a','b','c','c'],'number':[-1,7,50,36],'category':pd.Categorical(['apple','banana','orange','peach'])})
# print(df)
# print(df.describe())
# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.DataFrame({'shangpinga':[2,34,25,4],'shangpingb':[1,3,45,9],'shangpingc':[7,5,5,3]},index=['quarter1','quarter2','quarter3','quarter4'])
# print(df)
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei']
# df.plot(kind='bar',xlabel='quarter',ylabel='xiaoshoue',rot=0)
# plt.show()
# import numpy as np
# arr1=np.array([1,1,8])
# arr2=np.array([[1,2,4],[0,1,0],[0,0,2]])
# c=np.matmul(arr1,arr2)
# print(c)
# a=np.array([[-2,1,0],[-2,1,1],[-1,1,1]])
# A = np.matrix(a)
# print(A.I)
# d=np.matmul(arr1,A.I)
# print(d)
# import pandas as pd
# import numpy as np
# date1=pd.read_excel(r"ycl1.xls",usecols="A,B,C,D,E,F,G,H,N")
# print(date1)
# print('')
#
# print('检测缺失值')#检测所有数据的缺失值，如果有将该行删除，检测结果为无
# print(date1.isnull().sum())
# print('')
#
# print('检测年龄取值范围')#检测年龄的取值是否超出常理，是否在0到120之间
# print((date1['Age']>0).sum(),(date1['Age']<120).sum())
# print('')
#
# print('对胸部疼痛类型不做处理')
# print('')
#
# print('对血压进行离散化')#由于血压数据过于复杂，在分析时会不方便操作，于是将数据离散化，分类为五类
# cut=pd.cut(date1['Blood平静状态下的血压'],bins=[0,90,120,130,140,180])
# print(cut)
# print(cut.value_counts())
# print('')
# # print(cut.iloc[1])
# # for i in range(269):
# #     date1['Blood平静状态下的血压'].replace(date1['Blood平静状态下的血压'][i+1],cut.iloc[i], inplace=True)
# # print(date1['Blood平静状态下的血压'])
#
# print('对血清胆固醇含量进行离散化')#与血压同理
# cut1=pd.cut(date1['Serum血清胆固醇含量'],bins=[0,200,220,1000])
# print(cut1)
# print(cut1.value_counts())
# print('')
#
# print('对未进食状态下的血糖浓度不做处理')
# print('')
#
# print('对平静状态下心电图结果不做处理')
# print('')
#
# print('对最大心跳速率进行离散化')#与血压同理
# cut2=pd.cut(date1['Heartrate最大心跳速率'],bins=[0,100,140,200])
# print(cut2)
# print(cut2.value_counts())
# print('')


# import numpy as np
# arr2=np.array([[1,2,0,0],[2,3,0,0],[1,1,1,0],[1,0,0,1]])
# arr=np.array([[5,-2,-4,3],[3,-1,-3,2],[-3,0.5,4.5,-2.5],[-10,3,11,-7]])
# A = np.matrix(arr2)
# eigenvalue, featurevector = np.linalg.eig(arr)
# print("特征值：", eigenvalue)
# print("特征向量：", featurevector)9

# import pandas as pd
# import numpy as np
# date1=pd.read_excel(r"ycl1.xls")
# print(date1)
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# plt.title("bbbbb")
# plt.show()

#
# import pandas as pd
# import numpy as np
# date1=pd.read_excel(r"class222.xlsx")
# print(date1.head)
#
# print(date1.isnull().any())
# date2=date1.dropna()
# print(date2.shape)
# print(date2)
# print(date2.isnull().any())

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.shanghairanking.cn/institution/yunnan-university'
#
# # 发送请求并获取响应内容
# response = requests.get(url)
# html = response.content
#
# # 解析HTML页面
# soup = BeautifulSoup(html, 'html.parser')
#
# # 获取学生满意度和院校满意度
# satisfaction_box = soup.find_all('div', attrs={'class': 'cl-left-text'})
# student_satisfaction = satisfaction_box[0].find('span').text.strip()
# school_satisfaction = satisfaction_box[1].find('span').text.strip()
#
# # 进入学生满意度和院校满意度的具体页面
# student_url = url + '/student'
# school_url = url + '/survey'
#
# # 发送请求并获取响应内容
# student_response = requests.get(student_url)
# student_html = student_response.content
#
# school_response = requests.get(school_url)
# school_html = school_response.content
#
# # 解析HTML页面
# student_soup = BeautifulSoup(student_html, 'html.parser')
# school_soup = BeautifulSoup(school_html, 'html.parser')
#
# # 获取学生满意度的详细信息
# student_table = student_soup.find('table', attrs={'class': 'infor-table'})
# student_data = []
# for tr in student_table.find_all('tr')[1:]:
#     tds = tr.find_all('td')
#     student_data.append({
#         'category': tds[0].text.strip(),
#         'score': tds[1].text.strip(),
#         'percentage': tds[2].text.strip()
#     })
#
# # 获取院校满意度的详细信息
# school_table = school_soup.find('table', attrs={'class': 'infor-table'})
# school_data = []
# for tr in school_table.find_all('tr')[1:]:
#     tds = tr.find_all('td')
#     school_data.append({
#         'category': tds[0].text.strip(),
#         'total_score': tds[1].text.strip(),
#         'score': tds[2].text.strip(),
#         'percentage': tds[3].text.strip()
#     })
#
# print('学生满意度：', student_satisfaction)
# print('学生满意度的详细信息：', student_data)
# print('院校满意度：', school_satisfaction)
# print('院校满意度的详细信息：', school_data)







































































































