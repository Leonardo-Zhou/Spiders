# -*- coding: utf-8 -*-
"""
@File    : 测试requests下载文件.py
@Time    : 2022/2/19 0:00
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import requests
from USER_AGENT import UA_list
import random
from lxml import etree

# with open('proxies.txt','r') as file:
#     s = file.readlines()[1].replace('\n','')

headers = {
            'user-agent': random.choice(UA_list)
        }

url = 'https://p302.zlibcdn.com/dtoken/afb754c532d719a781499d6ccd012d07'
requests.get(url,headers)
