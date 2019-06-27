#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

import img.basev as ba

# 读取摄像头，若想读取视频，参数0换成视频的路径+文件名
cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(ba.TEMP_VIDEO)

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
