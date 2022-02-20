# -*- coding: utf-8 -*-
"""
@File    : 测试读写文件.py
@Time    : 2022/2/19 17:21
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
# proxy_list = ['a\n','n\n']
# 
# with open('a.txt', 'w') as file:
#     file.write(proxy_list)
import json

with open('BookList.json','r') as file:
    j = json.load(file)
    
print(j)