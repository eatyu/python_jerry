#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

print(cv2.__version__)

# 构建一张图
img = np.zeros([512, 512, 3], dtype=np.uint8)

# for i in img.size

print(img.imag)
# print(img.flags)
# print(img.nbytes)
# print(img.size)
# print(img.itemsize)
# print(img.ndim)

# 3通道
print(img.shape)

# 绘图 灰色 (会调用 windows 图片查看器之类的)
# img[256, 256] = [99, 99, 99]
# img2 = Image.fromarray(img, 'RGB')
# img2.save('my.png')
# img2.show()


for i in range(512):
    for j in range(512):
        img[i, j, :] = [i % 256, j % 256, (i + j) % 256]

# 绘图 （）
# plt.imshow(img)
# plt.show()


# 绘图 （自己的图片显示工具）
# 创建 窗口
cv2.namedWindow('custom image', cv2.WINDOW_NORMAL)

# 窗口中显示图像
cv2.imshow('custom image', img)
# 最后还要写一句代码，这样就可以使窗口始终保持住
cv2.waitKey(0)
cv2.destroyAllWindows()
