# -*- coding: utf-8 -*-
"""
@File    : test_xpath.py
@Time    : 2021/12/27 9:22
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

from lxml import etree

with open('c.html', 'rb') as file:
    content = file.read().decode('utf-8')

selector = etree.HTML(content)

# print(selector.xpath('//title')[0].xpath('./text()'))
# nodes = selector.xpath('//*[@id="J_goodsList"]/ul/li')
# print(nodes)
# for i in nodes[1:]:
#     if i.xpath('./@data-spu') == ['']:
#         print(1)
    # print(i.xpath('./@data-spu'))
    
print(' '.join(selector.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')[0].replace('\n','').split()))