# -*- coding: utf-8 -*-
"""
@File    : 测试selenium.py
@Time    : 2022/2/18 14:20
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

with open('proxies.txt','r') as file:
    proxy = file.readlines()[1].replace('\n','')


url = 'https://ca1lib.org/book/3697965/3cb076'


options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
options.add_experimental_option("prefs",prefs)
options.add_argument(' proxy-server=socks5://' + proxy)
browser = webdriver.Chrome(options=options)
browser.set_page_load_timeout(10)
browser.get(url)
download_button = browser.find_element_by_xpath('//a[@class="btn btn-primary dlButton addDownloadedBook"]')
print(type(download_button))


# browser = webdriver.Chrome()
# proxy = Proxy(
#     {
#         'proxyType': ProxyType.MANUAL,
#         'socksProxy5': '94.103.88.24:1080'
#     }
# )
# desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# proxy.add_to_capabilities(desired_capabilities)
#
# browser.start_session(desired_capabilities)
# browser.get(url)
