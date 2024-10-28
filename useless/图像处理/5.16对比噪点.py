import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)


def compare_diff(early_image_path,new_image_path):

    img0 = cv2.imread(early_image_path)
    img1 = cv2.imread(new_image_path)
    diffcerence = cv2.absdiff(img0,img1)
    print(diffcerence)

res = compare_diff('p1.png','p2.png')
