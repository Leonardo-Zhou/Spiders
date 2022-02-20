# -*- coding: utf-8 -*-
"""
@File    : download_page.py
@Time    : 2021/12/26 14:12
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
from lxml import etree
import json
import random


url = 'https://item-soa.jd.com/getWareBusiness?skuId=100016720344&cat=16750%2C16754%2C16800&area=1_72_2799_0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }


def ip_json_socks():
    with open('ip.json', 'r') as file:
        proxies = json.load(file)
        for ip_address in proxies:
            proxy = {
                "http": 'socks5://zhima:zhima@{}:{}/'.format(ip_address['ip'], ip_address['port']),
                "https": 'socks5://zhima:zhima@{}:{}/'.format(ip_address['ip'], ip_address['port'])
            }
            content = requests.get(url, headers=headers, proxies=proxy).content
            print(content)


def socks_5_text():
    with open('socks5.txt', 'r') as file:
        proxies = file.readlines()
        print(proxies)
        for ip_address in proxies:
            proxy = {
                "http": 'socks5://{}'.format(ip_address.replace('\n','')),
                # "https": 'socks5://{}:{}'.format(ip_address['ip'], ip_address['port'])
            }
            content = requests.get(url, headers=headers,proxies=proxy).content
            print(content)

          
def http_text():
    with open('http.txt', 'r') as file:
        proxies = file.readlines()
        print(proxies)
        for ip_address in proxies:
            proxy = {
                "http": 'http://{}'.format(ip_address.replace('\n','')),
                # "https": 'socks5://{}:{}'.format(ip_address['ip'], ip_address['port'])
            }
            content = requests.get(url, headers=headers,proxies=proxy).content
            print(content)


def use_cookies():
    headers['cookies'] = 'token=4131365db76d520ca1c86d9e9efc2921,1,911450; __jda=122270672.16406100941401313025812.1640610094.1640610094.1640610094.1; __jdb=122270672.1.16406100941401313025812|1.1640610094; __jdc=122270672; __jdv=122270672|direct|-|none|-|1640610094141; shshshfp=827362b9914b13f6c56b35ac15d8d1e5; shshshfpa=9fd957a5-c958-3df4-765f-1ab8ce22d2e9-1640610095; shshshsID=c5276410801d88f6d0cbdac262afab82_1_1640610095166; shshshfpb=eutNDpqabjePWjn41Zxq3gQ==; areaId=15; ip_cityCode=1262; ipLoc-djd=15-1262-1267-56327; 3AB9D23F7A4B3C9B=ZYW2JNUUDVQPM4OHDMCDJK2DCKZPUTOWMQIEMIHGM64Z2UMFKIDED6UF6EIHVYXSXYJ42O6KAJ4HPIP75PFUYSVPO4'
    print(requests.get(url,headers).content)


use_cookies()
