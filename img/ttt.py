#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

pic = cv2.imread('./temp2.jpg')
pic_1 = cv2.resize(pic, (400, 400), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('', pic)
# cv2.waitKey(0)
cv2.imshow('', pic_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
