import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)

def loss(y_true, y_pred):
    return (((y_true - y_pred) ** 2).mean())*0.5

class OurNeuralNetworks():
    def __init__(self):
        self.w1 = np.random.normal(0.0, 1.0)
        self.w2 = np.random.normal(0.0, 1.0)
        self.v1 = np.random.normal(0.0, 1.0)
        self.v2 = np.random.normal(0.0, 1.0)

    def feedforward(self, x):
        h1 = sigmoid(self.w1 * x)
        h2 = sigmoid(self.w2 * x)
        o1 = self.v1 * h1 + self.v2 * h2
        return o1

    def train(self, x_train, y_train, learning_rate=0.01, epochs=100):
        losses = []
        for epoch in range(epochs):
            for x, y_true in zip(x_train, y_train):
                h1 = sigmoid(self.w1 * x)
                h2 = sigmoid(self.w2 * x)
                o1 = self.v1 * h1 + self.v2 * h2

                grad_o1 = -(y_true - o1)

                grad_v1 = grad_o1 * h1
                grad_v2 = grad_o1 * h2
                grad_w1 = grad_o1 * self.v1 * deriv_sigmoid(self.w1 * x) * x
                grad_w2 = grad_o1 * self.v1 * deriv_sigmoid(self.w2 * x) * x

                self.w1 -= learning_rate * grad_w1
                self.w2 -= learning_rate * grad_w2
                self.v1 -= learning_rate * grad_v1
                self.v2 -= learning_rate * grad_v2

            if (epoch + 1) % 10 == 0:
                current_loss = loss(y_train, np.array([self.feedforward(xi) for xi in x_train]))
                losses.append(current_loss)

        return losses


# 定义训练集和测试集数据
n = 1000
input_data = np.random.normal(0, 1, n)
beta0 = 2
beta1 = 6
ips = np.random.normal(0, 1, n)
output_data = beta0 + beta1 * input_data + ips

x_train = input_data[:500]
y_train = output_data[:500]
x_test = input_data[500:]
y_test = output_data[500:]

# 创建网络实例并训练
network = OurNeuralNetworks()
losses = network.train(x_train, y_train, learning_rate=0.01,epochs=1000)

# 绘制损失函数随时间变化的图
plt.plot(losses, label='Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss per Generation')
plt.legend()
plt.show()

# 输出最终的权重和偏置值
print(f'Final weights and biases:')
print(f'w1: {network.w1}, w2: {network.w2}')
print(f'v1: {network.v1}, v2: {network.v2}')
