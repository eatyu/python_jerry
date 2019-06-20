#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 通过opencv 处理图片


# 读取 显示

img = cv2.imread('temp2.jpg', cv2.IMREAD_UNCHANGED)
print(img)
print(np.shape(img))

cv2.namedWindow("temp2 IMAGE", cv2.WINDOW_AUTOSIZE)
cv2.imshow("temp2 IMAGE", img)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite("temp2_copy.jpg", img)
