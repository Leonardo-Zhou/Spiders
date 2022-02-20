# -*- coding: utf-8 -*-
"""
@File    : test_json.py
@Time    : 2021/12/26 11:58
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import json
import jsonpath

with open('a.html','rb') as file:
    # c = json.load(file)
    content = file.read().decode('utf-8')

c = json.loads(content)
print(c['price'])