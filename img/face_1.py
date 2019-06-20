#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
# sys.path.append(r"D:\projects\python\pathon_jerry")

import cv2

import img.basev as ba

temp_img = ba.TEMP_FACE_IMG

classfier = cv2.CascadeClassifier(ba.cc_default)

# 读取图片
image = cv2.imread(temp_img)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = classfier.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("发现{0}个人脸!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)
    # print(type((x + x + w) / 2))
    # cv2.circle(image, ((x + x + w) / 2, (y + y + h) / 2), w / 2, (0, 255, 0), 2)

cv2.imshow("Find Faces!", image)
cv2.waitKey(0)
