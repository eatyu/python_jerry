#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

import img.basev as ba

# 读取摄像头，若想读取视频，参数0换成视频的路径+文件名
cap = cv2.VideoCapture(0)
print(cap.isOpened())
cap.open(0)
print(cap.isOpened())
# 摄像头 调用不了 因为没有摄像头

cap = cv2.VideoCapture(ba.TEMP_VIDEO)
print(cap.isOpened())

while (True):
    print(cap.get(cv2.CAP_OPENNI_GRAY_IMAGE))

    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:  # esc
        # if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
