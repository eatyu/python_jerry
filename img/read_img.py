#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img_url = r'C:\ProjectResourceDownload\crawler\zhihu\v2-a53f33209dc63eeb6c422a901d25da98_hd.jpg'
img = np.array(Image.open(img_url))  # 打开当前目录图像并转化为数字矩阵
plt.figure("lena")
plt.imshow(img)
plt.axis('off')
plt.show()


