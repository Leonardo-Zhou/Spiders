# -*- coding: utf-8 -*-
"""
@File    : 测试日志收集.py
@Time    : 2021/11/22 20:50
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import time
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('w3c', False)
caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}


driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
driver.get('https://www.jssrvpn.xyz/auth/register')
verify_button = WebDriverWait(
                driver, 5, 0.5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "geetest_radar_tip")))
verify_button.click()
print('button clicked')
time.sleep(3)

d = driver.get_log('performance')
print(len(d))

with open('log.txt', 'a') as file:
    for log in d:
        file.write(str(log)+'\n')
        

