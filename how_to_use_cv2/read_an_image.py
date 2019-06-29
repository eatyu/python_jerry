#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

# 下面的import 是一样的
# import img.basev as ba
from img import basev as ba

image = cv2.imread(ba.TEMP_IMG, cv2.IMREAD_UNCHANGED)
cv2.imshow('img1', image)
cv2.imshow('img2', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
