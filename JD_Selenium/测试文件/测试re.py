# -*- coding: utf-8 -*-
"""
@File    : 测试re.py
@Time    : 2022/2/11 22:56
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import re

with open('test1.html','rb') as file:
    content = file.read().decode('utf-8')
    
pattern = re.compile('(.*\n)*.*colorSize: (\\[{.*?}*\\])')
print(re.match(pattern,content)[2])
