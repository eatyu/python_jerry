#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

img_url = r'C:\ProjectResourceDownload\crawler\zhihu\v2-a53f33209dc63eeb6c422a901d25da98_hd.jpg'

pil_im = Image.open(img_url).convert('L')

# 使用 crop() 方法可以从一幅图像中裁剪指定区域
box = (100, 100, 400, 400)
region = pil_im.crop(box)
region.save('bbb.jpg')

# thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小）
pil_im.thumbnail((128, 128))
pil_im.save('aaa.jpg')
