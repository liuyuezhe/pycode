import numpy as np
import matplotlib.pyplot as plt

# 参数设定
d = 100  # 河宽，单位：米
v1 = 1   # 河水流速，单位：米/秒
v2 = 2   # 小船在静水中的速度，单位：米/秒
k = v1 / v2  # 速度比
dt = 0.1  # 时间步长，单位：秒

# 计算横向和纵向速度分量
vx = v1
vy = v2 * np.sqrt(1 - k**2)

# 初始化位置和时间
x = 0
y = 0
t = 0

# 保存位置和时间数据
positions = [(x, y)]
times = [t]

# 数值求解
while y < d:
    x += vx * dt
    y += vy * dt
    t += dt
    positions.append((x, y))
    times.append(t)

# 提取位置数据
xs, ys = zip(*positions)

# 解析解路径
x_analytical = np.linspace(0, vx * (d / vy), 100)
y_analytical = vy / vx * x_analytical

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(xs, ys, label='Numerical Solution', linestyle='-', marker='o')
plt.plot(x_analytical, y_analytical, label='Analytical Solution', linestyle='--')
plt.xlabel('x (meters)')
plt.ylabel('y (meters)')
plt.title('Boat Crossing River')
plt.legend()
plt.grid(True)
plt.show()

# 输出渡河所需时间
渡河时间 = times[-1]
渡河时间
