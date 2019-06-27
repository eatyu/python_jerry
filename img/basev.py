#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

VIDEO_PATH = r'..\DoVideo'
IMG_PATH = r'..\DoVideo\Img'

TEMP_VIDEO = r'..\DoVideo\1091662177785761792.mp4'
TEMP_IMG = r'..\DoVideo\Img\temp.jpg'
TEMP_FACE_IMG = r'..\DoVideo\Img\Snipaste_2019-06-20_21-35-42.jpg'

cc_alt2 = r"C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml"

cc_default = r"C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"


# get file name without suffix
def get_name(path):
    _, tail_name = os.path.split(path)
    filename, _ = os.path.splitext(tail_name)
    return filename
