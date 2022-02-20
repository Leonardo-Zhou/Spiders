# -*- coding: utf-8 -*-
"""
@File    : 测试selenium.py
@Time    : 2021/12/27 20:51
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from USER_AGENT import UA_list
import random
import time

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent={}'.format(random.choice(UA_list)))
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)
# url = 'https://item-soa.jd.com/getWareBusiness?skuId=100028140632&cat=670%2C671%2C673&area=1_72_2799_0'
url = 'https://item.jd.com/100014794825.html'
url1 = 'https://item.jd.com/10028553618103.html'

browser.get(url)
# title = browser.find_element_by_xpath('//*[@class="sku-name"]').text
# print(title)
with open('test.html','wb') as file:
    file.write(browser.page_source.encode("utf-8", "ignore"))

time.sleep(500)