import numpy as np

# 计算熵
def calculate_entropy(y):
    class_labels = np.unique(y)
    entropy = 0
    for cls in class_labels:
        p = len(y[y == cls]) / len(y)
        entropy -= p * np.log2(p)
    return entropy

# 计算信息增益
def calculate_gain(data, feature, target):
    total_entropy = calculate_entropy(data[target])
    values, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = sum((counts[i] / sum(counts)) * calculate_entropy(data.where(data[feature] == values[i]).dropna()[target]) for i in range(len(values)))
    gain = total_entropy - weighted_entropy
    return gain

# ID3算法
def id3(data, original_data, features, target_attribute_name, parent_node_class=None):
    # 如果所有的值都相同，返回这个值
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    # 如果数据为空，返回原始数据中最常见的目标属性
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]
    # 如果没有更多的特征，返回父节点类别中最常见的
    elif len(features) == 0:
        return parent_node_class
    # 构建树
    else:
        # 设置默认值为当前节点中最常见的目标属性
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        
        # 选择信息增益最高的特征
        item_values = [calculate_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        # 创建树结构
        tree = {best_feature: {}}
        
        # 移除已经被选为最佳特征的特征
        features = [i for i in features if i != best_feature]
        
        # 递归构建决策树
        for value in np.unique(data[best_feature]):
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = id3(sub_data, original_data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree
        
        return tree

# 数据集
data = {
    '年级': ['青年', '青年', '青年', '青年', '青年', '中年', '中年', '中年', '中年', '中年', '老年', '老年', '老年', '老年', '老年'],
    '有无工作': ['否', '否', '是', '是', '否', '否', '否', '是', '否', '否', '否', '否', '是', '是', '否'],
    '有自己的房子': ['否', '否', '否', '是', '否', '否', '否', '是', '是', '是', '是', '是', '否', '否', '否'],
    '信用额度': ['一般', '好', '好', '一般', '一般', '一般', '好', '好', '非常好', '非常好', '非常好', '好', '好', '非常好', '一般'], 
    '类别': ['否', '否', '是', '是', '否', '否', '否', '是', '是', '是', '是', '是', '是', '是', '否']
}

# 转换为DataFrame
import pandas as pd
df = pd.DataFrame(data)

# 特征列表
features = df.columns.tolist()
features.remove('类别')

# 构建决策树
tree = id3(df, df, features, '类别')
print(tree)
