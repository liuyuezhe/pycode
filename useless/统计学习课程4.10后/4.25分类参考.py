import numpy as np

# 参数
n = 500
beta0_initial = 5
beta1_initial = 3
tolerance=1e-6  #容忍度
max_iter=1000   #最大迭代次数

# 生成一个服从正态分布的 x 值样本
x = np.random.normal(0, 1, (n, 1))

p = np.exp(beta0_initial + beta1_initial * x) / (1 + np.exp(beta0_initial + beta1_initial * x))
# 根据计算得到的概率 p 生成二元结果 y
y = np.random.binomial(1, p)

def newton_method(x, y, beta0_initial, beta1_initial, tolerance, max_iterations):
    # 牛顿法优化的函数
    beta0 = beta0_initial
    beta1 = beta1_initial
    for _ in range(max_iterations):
        # 使用当前beta值计算概率
        p = np.exp(beta0 + beta1 * x) / (1 + np.exp(beta0 + beta1 * x))
        # 计算梯度和Hessian矩阵
        gradient_beta0 = np.mean(p - y)
        gradient_beta1 = np.mean(x * (p - y))
        hessian_beta0_beta0 = np.mean(p * (1 - p))
        hessian_beta1_beta1 = np.mean(x * x * p * (1 - p))
        hessian_beta0_beta1 = np.mean(x * p * (1 - p))
        hessian_beta1_beta0 = hessian_beta0_beta1
        # 构建梯度和Hessian矩阵
        gradient = np.array([gradient_beta0, gradient_beta1])
        hessian = np.array([[hessian_beta0_beta0, hessian_beta0_beta1],
                            [hessian_beta1_beta0, hessian_beta1_beta1]])
        # 使用牛顿法求解步长
        step = np.linalg.solve(hessian, -gradient)
        # 更新beta值
        beta0 += step[0]
        beta1 += step[1]
        # 检查收敛性
        if np.linalg.norm(step) < tolerance:
            break
    return beta0, beta1

# 运行牛顿迭代
beta0, beta1 = newton_method(x, y, beta0_initial, beta1_initial, tolerance, max_iter)

# 输出结果
print("beta0:", beta0)
print("beta1:", beta1)