# -*- coding: utf-8 -*-
"""
@File    : 获得网址.py
@Time    : 2021/11/23 9:20
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import re

with open('log.txt','r') as file:
    data = file.readlines()
    compiled = re.compile(r'.*(https://static.geetest.com/pictures/gt/.*\.png)')
    for line in data:
        temp = compiled.match(line)
        if temp:
            print(temp.group(1))
            break
