#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import cv2

import img.basev as ba

# 图片存放根目录
base_img_dir = ba.IMG_PATH


def get_imgs(path):
    name = ba.get_name(ba.TEMP_VIDEO)
    img_dir = base_img_dir + "/" + name
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    # 提取面部图片
    cap = cv2.VideoCapture(path)
    suc = cap.isOpened()
    cap.set(1, 90)  # Where frame_no is the frame you want
    ret, frame = cap.read()  # Read the frame
    cv2.imshow('window_name', frame)
    cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 参数为视频地址
    video_url = ba.TEMP_VIDEO
    get_imgs(video_url)
