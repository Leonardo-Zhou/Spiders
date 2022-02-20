# -*- coding: utf-8 -*-
"""
@File    : 测试socks代理.py
@Time    : 2022/2/18 19:34
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
from USER_AGENT import UA_list
import random
from lxml import etree

with open('proxies.txt','r') as file:
    s = file.readlines()[0].replace('\n','')

headers = {
            'user-agent': random.choice(UA_list)
        }
url = 'https://ca1lib.org/s/Python?'

session = requests.session()
my_proxies={"http": "socks5h://{}".format(s),"https": "socks5h://{}".format(s)}

i = 0

def d(m):
    try:
        m += 1
        r = session.get(url=url, timeout=15,headers=headers).content.decode('utf-8')
        return r
    except Exception as e:
        print(e)
        with open('proxies.txt', 'r') as file:
            s = file.readlines()[m].replace('\n', '')
        print('加载失败')
        d(m)

# selector = etree.HTML(r)
# url = 'https://ca1lib.org' + selector.xpath('//a[@class="btn btn-primary dlButton addDownloadedBook"]/@href')[0]
# r = session.get(url,proxies=my_proxies,headers=headers)
# url = r.headers['location']
# print(url)
# with open('aa.html','wb') as file:
#     file.write(r.content)
r = d(i)
print(dir(r))
# print(r.headers)