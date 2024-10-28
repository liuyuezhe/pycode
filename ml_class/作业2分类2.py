import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, roc_auc_score
from sklearn.tree import plot_tree

# 1. 数据加载
data = pd.read_csv('titanic.csv')

# 2. 数据清洗
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data = data.drop(['Cabin', 'Ticket', 'Name'], axis=1)

# 分类变量转换为数值
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})  # 将登船港口转换为数值

# 3. 特征选择
features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']

# 4. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 建模
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. 预测
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # 获取预测的概率

# 7. 评估模型
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print('Accuracy:', accuracy)
print('F1 Score:', f1)
print('ROC AUC Score:', roc_auc)
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))

# 8. 可视化决策树
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=features, class_names=['Not Survived', 'Survived'], filled=True)
plt.title('Decision Tree Visualization')
plt.show()
