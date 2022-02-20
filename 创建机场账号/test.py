# -*- coding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/11/22 18:42
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


server = Server(r'C:\Users\29745\PycharmProjects\spider\创建机场账号\browsermob-proxy-2.1.4\bin\browsermob-proxy')
server.start()
proxy = server.create_proxy()

chrome_options = Options()
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

driver = webdriver.Chrome(chrome_options=chrome_options)