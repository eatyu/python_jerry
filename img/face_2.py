#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

import img.basev as ba

temp_video = ba.TEMP_VIDEO
img_path = ba.IMG_PATH
name = 'tooooom'


def getface(path):
    cap = cv2.VideoCapture(path)
    classfier = cv2.CascadeClassifier(r"C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    out_count = 0
    while suc:
        frame_count += 1
        if out_count > 100:  # 最多取出多少张
            break
        suc, frame = cap.read()  # 读取一帧
        params = []
        params.append(2)  # params.append(1)
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))  # 读取脸部位置

        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转为灰度图
                cv2.imshow("Find Faces!", image)
                cv2.waitKey(0)
                cv2.imwrite(img_path + 'waitdel.jpg', image)

            out_count = 101
        #
        # if len(faceRects) > 0:  # 大于0则检测到人脸
        #     for faceRect in faceRects:  # 单独框出每一张人脸
        #         x, y, w, h = faceRect
        #         image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
        #         image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转为灰度图
        #         img_new = cv2.resize(image, (57, 57), interpolation=cv2.INTER_CUBIC)  # 处理面部的大小
        #         cv2.imshow("Find Faces!", image)
        #         cv2.imwrite('C:/DoVideo/img/' + name + '/%d.jpg' % out_count, img_new, params)  # 存储到指定目录
        #         out_count += 1
        #         print('成功提取' + name + '的第%d个脸部' % out_count)
        #         break  # 每帧只获取一张脸，删除这个即为读出全部面部
        #


if __name__ == '__main__':
    getface(temp_video)  # 参数为视频地址
