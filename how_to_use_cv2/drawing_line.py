#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
print(img)

# Draw a diagonal blue line with thickness of 5 px
line = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow('line', line)

rectangle = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.imshow('rectangle', rectangle)

circle = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv2.imshow('circle', circle)

ellipse = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (96, 96, 96), -1)
cv2.imshow('ellipse', ellipse)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
polylines = cv2.polylines(img, [pts], True, (0, 255, 255))

# 添加文字
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('polylines', polylines)
cv2.waitKey(0)
