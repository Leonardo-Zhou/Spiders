# -*- coding: utf-8 -*-
"""
@File    : JDSpider.py
@Time    : 2021/12/27 20:24
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
import Data_parsers


def options():
    """
    :return: 浏览器设置
    """
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--user-agent={}'.format(random.choice(UA_list)))
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options


class JDSpider:
    def __init__(self, keyword, n):
        chrome_options = options()
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.keyword = keyword
        self.url = 'https://search.jd.com/Search?keyword={}&page='.format(keyword)
        self.max_num = n
        self.parser = Data_parsers.parser()
        self.tool = Data_parsers.Tools()
        
    def download_page(self):
        """
        使用selenium下载页面的内容
        :return: 页面content
        """
        content = self.browser.page_source
        return content
    
    def get_init_page(self, page_num):
        """
        获得搜索页面文本内容
        :param page_num: 第几页
        :return: 页面内容
        """
        self.browser.get(self.url + str(page_num+1))
        con = self.download_page()
        return con
    
    def run(self):
        for i in range(self.max_num):
            content = self.get_init_page(i)
            url_list = self.parser.parse_init_page(content)
            for url in url_list:
                self.browser.get(url)
                content = self.download_page()
                information, sku_id_list = self.parser.parse_page(content, first_page=True)
                print(information)
                for sku_id in sku_id_list:
                    url = 'https://item.jd.com/{}.html'.format(sku_id['skuId'])
                    self.browser.get(url)
                    content = self.download_page()
                    information,_ = self.parser.parse_page(content, first_page=False)
                    print(information)
                    
                    
                
                
        
                
    
if __name__ == '__main__':
    spider = JDSpider('r9000p',1)
    spider.run()
    
    
            