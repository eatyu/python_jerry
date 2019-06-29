#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import cv2

import img.basev as ba

# 图片存放根目录
base_img_dir = ba.IMG_PATH


def get_imgs(path):
    classfier = cv2.CascadeClassifier(ba.cc_alt2)

    # 创建存储图片的文件夹
    img_dir = get_dir_name()
    # 提取面部图片
    cap = cv2.VideoCapture(path)
    suc = cap.isOpened()

    while suc:
        suc, frame = cap.read()
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  #
                cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2, lineType=cv2.LINE_8)
                cv2.imshow("Find Faces!", image)
                # cv2.waitKey(0)
                break  # 每帧只获取一张脸，删除这个即为读出全部面部

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == 27:  # esc
            # if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def get_dir_name():
    name = ba.get_name(ba.TEMP_VIDEO)
    img_dir = base_img_dir + "/" + name
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return img_dir


if __name__ == '__main__':
    # 参数为视频地址
    video_url = ba.TEMP_VIDEO
    get_imgs(video_url)
