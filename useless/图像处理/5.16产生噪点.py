import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)
def random_noise(image_path, noise_num):

    img = cv2.imread(image_path,0)
    rows, cols= img.shape

    for i in range(noise_num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y] = 255  # 设置像素点为白色，产生噪声

    return img

# 使用示例
image_with_noise = random_noise('p1.png', 5000)
cv2.imshow('Image with Random Noise', image_with_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('p2.png',image_with_noise)
