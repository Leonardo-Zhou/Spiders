# -*- coding: utf-8 -*-
"""
@File    : 测试直接打开图片.py
@Time    : 2021/11/23 12:35
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
import cv2
import numpy as np

url = 'https://static.geetest.com/pictures/gt/95e6a13e6/slice/c68c29a75.png'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

response = requests.get(url,headers=headers)
image = cv2.imdecode(np.asarray(bytearray(response.content),dtype='uint8'), cv2.IMREAD_COLOR)

cv2.imshow('Show',image)
cv2.waitKey(0)

image1 = cv2.imread('target.png')
cv2.imshow('Show',image1)
cv2.waitKey(0)