# -*- coding: utf-8 -*-
"""
@File    : test_ip.py
@Time    : 2021/12/26 22:53
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
from lxml import etree

from USER_AGENT import UA_list
import random
import json
import time

base_url = 'https://item-soa.jd.com/getWareBusiness?skuId=100022009682&cat=670,677,679&area=15_1158_46341_46352'
headers = {
    'User-Agent': random.choice(UA_list)
}

with open('ip.json', 'r') as file:
    proxies = json.load(file)
    print(proxies)
    num = 1
    time.sleep(2)
    for i in proxies:
        proxy = {
            "http": "https//" + i['ip'] + ':' + str(i['port'])
        }
        print(requests.get(base_url,headers=headers,proxies=proxy).status_code)
        with open('{}.html'.format(num), 'wb') as file:
            file.write(requests.get(base_url,headers=headers,proxies=proxy).content)
        num += 1
        #
        # wb_data = requests.get(url=base_url, headers=headers, proxies=proxy).content.decode('utf-8')
        # content = etree.HTML(wb_data)
        # print(content.xpath('//*[@id="rightinfo"]/dl/dd[1]/text()')[0])
 