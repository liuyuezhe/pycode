import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, f1_score
from sklearn.preprocessing import label_binarize

# 加载数据集
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# 查看数据的前几行
# print(data.head())

# 检查数据类型和缺失值
# print(data.info())
# print(data.isnull().sum())

# 绘制配对图
# sns.pairplot(data, hue='species')
# plt.show()

# 区分训练集和数据集
X = data.iloc[:, :-1]  # 特征
y = data['species']     # 标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5 , random_state=42)

# 用决策树进行建模,并预测
clf = DecisionTreeClassifier(random_state=42,max_depth=2)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 预测概率用于计算AUC
y_pred_prob = clf.predict_proba(X_test)

# 模型评价：acc准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('----------------------------------------------------------------')

# 计算AUC（使用“one-vs-rest”策略）
# 将y转换为二进制格式
y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
y_pred_prob_bin = y_pred_prob  # 直接使用predict_proba

# 计算AUC
auc_scores = {}
for i in range(3):  # 有三类
    auc = roc_auc_score(y_test_bin[:, i], y_pred_prob_bin[:, i])
    auc_scores[iris.target_names[i]] = auc
print("AUC Scores:")
for species, score in auc_scores.items():
    print(f'{species}: {score:.2f}')
print('----------------------------------------------------------------')

# f1-score
f1 = f1_score(y_test, y_pred, average='weighted')
print(f'F1 Score: {f1:.2f}')
