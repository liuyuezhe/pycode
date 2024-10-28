import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 读取数据，得到因变量和自变量
datas = pd.read_excel('数据t1.xlsx', sheet_name='Sheet1', header=None)
datas = datas.iloc[1:, 1:3]
datas = datas.to_numpy()
num_of_people = datas[:, 0]  # 自变量
income = datas[:, 1]  # 因变量

#处理数据格式以及缺失值
for i in range(len(income)):
    float(income[i])
    float(num_of_people[i])
    if np.isnan(income[i]):
        income[i] = 0
        num_of_people[i] = 0
income = income[income != 0]
num_of_people = num_of_people[num_of_people != 0]

# 线性回归
# 训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(num_of_people.reshape(-1, 1), income.reshape(-1, 1),test_size=0.2,shuffle = True,random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
#求mse
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# 绘制散点图和回归线
plt.scatter(num_of_people, income, color='blue', label='Actual data')
plt.plot(X_test, y_pred, color='red', label='Fitted line')
plt.title('Linear Regression Fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()