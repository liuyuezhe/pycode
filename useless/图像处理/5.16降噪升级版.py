import cv2
import numpy as np

# 读取图像
img = cv2.imread('p2.png', cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图像

# 设置降噪参数
h = 10  # h参数调节过滤器强度。较大的h值可以更好地消除噪点，但也可能消除图像细节
templateWindowSize = 7  # templateWindowSize用于计算权重的模板补丁的像素大小，为奇数
searchWindowSize = 21  # searchWindowSize窗口的像素大小，用于计算给定像素的加权平均值，为奇数

# 使用fastNlMeansDenoising降噪
dst = cv2.fastNlMeansDenoising(img, None, h, templateWindowSize, searchWindowSize)

# 显示原图和降噪后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Denoised Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

    