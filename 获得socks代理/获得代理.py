# -*- coding: utf-8 -*-
"""
@File    : 获得代理.py
@Time    : 2022/2/19 12:31
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
from selenium import webdriver


def init_webdriver():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "C:\\Users\\29745\\PycharmProjects\\spider\\获得socks代理"}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    return options


class GetIP:
    def __init__(self,target_website,web_title):
        self.url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'
        self.options = init_webdriver()
        self.browser = webdriver.Chrome(options=self.options)
        self.target_website = target_website
        self.web_title = web_title

    def download(self):
        self.browser.get(self.url)
        
    def test_ip(self):
        with open('socks5_proxies.txt','r') as file:
            proxy_list = file.readlines()
        for proxy in proxy_list:
            proxy.replace('\n','')
            
        
        