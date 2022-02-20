# -*- coding: utf-8 -*-
"""
@File    : 解析网页文件.py
@Time    : 2021/11/23 15:54
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import re
from lxml import etree
with open('after.html','rb') as file:
    content = file.read().decode('utf-8')
    
selector = etree.HTML(content)
url = selector.xpath('//div[@class="buttons"]/a[7]/@data-clipboard-text')
print(url)
