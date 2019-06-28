#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import img.basev as ba

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.isOpened())

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
