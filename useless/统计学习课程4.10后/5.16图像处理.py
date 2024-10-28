import cv2
import numpy as np


def random_noise(image_path, noise_num):

    img = cv2.imread(image_path)
    rows, cols,_ = img.shape

    for i in range(noise_num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y] = 255  # 设置像素点为白色，产生噪声

    return img

# 使用示例
image_with_noise = random_noise('C:\\Users\\84478\\Desktop\\p1.png', 500000)
cv2.imshow('Image with Random Noise', image_with_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()
