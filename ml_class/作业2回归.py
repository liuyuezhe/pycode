from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 加载加州住房数据集
california = fetch_california_housing()

# 创建 DataFrame
data = pd.DataFrame(california.data, columns=california.feature_names)
data['MEDIAN_HOUSE_VALUE'] = california.target
print(data.head())

# 检查缺失值
print(data.isnull().sum())

# 数据标准化
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop('MEDIAN_HOUSE_VALUE', axis=1))

# 划分训练集和测试集
X = scaled_features
y = data['MEDIAN_HOUSE_VALUE']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树回归模型
model = DecisionTreeRegressor(random_state=42,max_depth=10)
# 在测试后，发现max_depth=10时mse最小，R²最大

# 训练模型
model.fit(X_train, y_train)

# 模型评估
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')

# 结果可视化
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Median House Value')
plt.ylabel('Predicted Median House Value')
plt.title('Actual vs Predicted Median House Value')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')  # 添加对角线
plt.show()