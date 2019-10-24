#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

VIDEO_PATH = r'..\DoVideo'
IMG_PATH = r'..\DoVideo\Img'

TEMP_VIDEO = r'..\DoVideo\1091662177785761792.mp4'
TEMP_VIDEO2 = r'..\DoVideo\1041395139956232192.mp4'
TEMP_IMG = r'..\DoVideo\Img\temp.jpg'
TEMP_FACE_IMG = r'..\DoVideo\Img\Snipaste_2019-06-20_21-35-42.jpg'

cc_alt2 = r"C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml"

# conda托管下 python_jerry虚拟环境中的opencv2自带的人脸样本文件位置
cc_alt2_conda = r"C:\Miniconda3\envs\python_jerry\Library\etc\haarcascades\haarcascade_frontalface_alt2.xml"

cc_default = r"C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"

cc_default_conda = r"C:\Miniconda3\envs\python_jerry\Library\etc\haarcascades\haarcascade_frontalface_default.xml"


# get file name without suffix
def get_name(path):
    _, tail_name = os.path.split(path)
    filename, _ = os.path.splitext(tail_name)
    return filename
