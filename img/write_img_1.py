#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

video_path = 'C:/DoVideo/Img/'
img_path = r'./temp.jpg'
img = cv2.imread(img_path)

cv2.imwrite(video_path + "temp_copy_1.jpg", img)
