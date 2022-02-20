# -*- coding: utf-8 -*-
"""
@File    : 测试下载.py
@Time    : 2022/2/19 12:22
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

from selenium import webdriver


url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\Users\\29745\\PycharmProjects\\spider\\获得socks代理"}
options.add_experimental_option("prefs", prefs)
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get(url)
