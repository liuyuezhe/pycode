import numpy as np
import matplotlib.pyplot as plt
# 定义 sigmoid 函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# 假设输入值x，目标值y_target
x = np.array([1.0])  # 示例输入值
y_target = np.array([2.0])  # 示例目标值

# 随机初始化权重和偏置
w1 = np.random.randn()
w2 = np.random.randn()
W3 = np.random.randn()
W4 = np.random.randn()
b1 = np.random.randn()
b2 = np.random.randn()
b3 = np.random.randn()

# 定义前向传播
def forward(x, w1, w2, W3, W4, b1, b2, b3):
    u1 = sigmoid(w1 * x + b1)
    u2 = sigmoid(w2 * x + b2)
    y = W3 * u1 + W4 * u2 + b3
    return u1, u2, y

# 定义损失函数
def loss(y, y_target):
    return 0.5 * (y - y_target) ** 2

# 定义损失函数对各参数的梯度
def gradients(x, y, y_target, u1, u2, w1, w2, W3, W4, b1, b2, b3):
    dy = y - y_target
    dW3 = dy * u1
    dW4 = dy * u2
    db3 = dy
    du1 = dy * W3
    du2 = dy * W4
    dw1 = du1 * sigmoid_derivative(w1 * x + b1) * x
    dw2 = du2 * sigmoid_derivative(w2 * x + b2) * x
    db1 = du1 * sigmoid_derivative(w1 * x + b1)
    db2 = du2 * sigmoid_derivative(w2 * x + b2)
    return dw1, dw2, dW3, dW4, db1, db2, db3

# 牛顿迭代法更新参数
def newton_step(x, y_target, w1, w2, W3, W4, b1, b2, b3, learning_rate=0.01):
    u1, u2, y = forward(x, w1, w2, W3, W4, b1, b2, b3)
    l = loss(y, y_target)
    dw1, dw2, dW3, dW4, db1, db2, db3 = gradients(x, y, y_target, u1, u2, w1, w2, W3, W4, b1, b2, b3)
    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2
    W3 -= learning_rate * dW3
    W4 -= learning_rate * dW4
    b1 -= learning_rate * db1
    b2 -= learning_rate * db2
    b3 -= learning_rate * db3
    return w1, w2, W3, W4, b1, b2, b3, l

# 训练网络
for epoch in range(1000):
    w1, w2, W3, W4, b1, b2, b3, l = newton_step(x, y_target, w1, w2, W3, W4, b1, b2, b3)
    if epoch % 20 == 0:
        plt.scatter(epoch,l)

print("Trained weights and biases:")
print(f"w1: {w1}, w2: {w2}, W3: {W3}, W4: {W4}, b1: {b1}, b2: {b2}, b3: {b3}")
plt.show()