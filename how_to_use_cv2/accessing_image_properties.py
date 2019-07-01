#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

import img.basev as ba

img = cv2.imread(ba.TEMP_IMG, cv2.IMREAD_UNCHANGED)

print(img.dtype)

img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

print(img.shape)
print(np.shape(img))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('a', img)
cv2.waitKey(0)
