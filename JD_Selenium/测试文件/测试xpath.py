# -*- coding: utf-8 -*-
"""
@File    : 测试xpath.py
@Time    : 2022/2/11 16:50
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
from lxml.etree import HTML

price = {}
with open('test.html', 'rb') as file:
    con = file.read().decode('utf-8')

selector = HTML(con)
p_price = selector.xpath('//span[@class="price J-p-%s"]/text()' % '100014794825')
try:
    student_price = selector.xpath('//div[@class="student-price"]/em/text()')[0]
except:
    student_price = None
    
try:
    active_price = selector.xpath('//div[@class="activity-price"]/span/text()')[0]
except:
    active_price = None
price['正常价格'] = p_price
price['学生价'] = student_price
price['活动价'] = active_price
print(price)
