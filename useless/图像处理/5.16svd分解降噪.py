import numpy as np
import cv2

# 读取图像并转换为灰度图
image = cv2.imread('p2.png',0)

# 应用SVD
U, S, Vt = np.linalg.svd(image, full_matrices=False)

# 初始化最小MSE和最佳k值
min_mse = np.inf
best_k = 0

# 尝试不同的k值以找到最小MSE
for k in range(1, len(S)):
    # 重构图像
    reconstructed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
    # 计算MSE
    mse = np.mean((image - reconstructed_image) ** 2)
    print(mse)
    # 更新最小MSE和最佳k值
    if mse < min_mse:
        min_mse = mse
        best_k = k

# 使用最佳k值重构图像
reconstructed_image = np.dot(U[:, :best_k], np.dot(np.diag(S[:best_k]), Vt[:best_k, :]))

# 保存和显示结果
denoised_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)
cv2.imwrite('denoised_image.jpg', denoised_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()





