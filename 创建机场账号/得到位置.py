# -*- coding: utf-8 -*-
"""
@File    : 得到位置.py
@Time    : 2021/11/23 8:31
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import cv2
import numpy as np


def show(name):
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    otemp = 'la.png'
    oblk = 'ori.png'
    target = cv2.imread(otemp, 0)
    template = cv2.imread(oblk, 0)
    w, h = target.shape[::-1]
    temp = 'temp.jpg'
    targ = 'targ.jpg'
    cv2.imwrite(temp, template)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    template = cv2.imread(temp)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    # 展示圈出来的区域
    cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
    show(target)
    show(template)


def template_demo():
    tpl = cv2.imread("la.png")
    target = cv2.imread("ori.png")
    cv2.imshow("template image",tpl)
    cv2.imshow("target image",target)
    methods = [cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        result = cv2.matchTemplate(target,tpl,md)
        # result是我们各种算法下匹配后的图像
        # cv.imshow("%s"%md,result)
        #获取的是每种公式中计算出来的值，每个像素点都对应一个值
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if md == cv2.TM_SQDIFF_NORMED:
            tl = min_loc    #tl是左上角点
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)    #右下点
        cv2.rectangle(target,tl,br,(0,0,255),2)   #画矩形
        cv2.imshow("match-%s"%md,target)


def identify_gap(bg, tp, out):
    # 识别图片边缘
    
    bg_edge = cv2.Canny(bg, 100, 200)
    
    tp_edge = cv2.Canny(tp, 100, 200)
    
    # 转换图片格式
    
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    
    # 缺口匹配
    
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    
    # 绘制方框
    
    th, tw = tp_pic.shape[:2]
    
    tl = max_loc  # 左上角点的坐标
    
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    
    cv2.rectangle(bg, tl, br, (0, 0, 255), 2)  # 绘制矩形
    
    cv2.imwrite(out, bg)  # 保存在本地
    
    # 返回缺口的X坐标
    return tl[0]


def crop_image(x_start, filename):
    img_temp = cv2.imread(filename)
    img = img_temp[0:, x_start:]
    return img

    
    


if __name__ == '__main__':
    verification_image = crop_image(50,'verification.png')
    target_image = cv2.imread('target.png')
    x = identify_gap(verification_image, target_image,'out.png')
    print(x)
