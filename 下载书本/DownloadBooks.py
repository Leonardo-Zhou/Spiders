# -*- coding: utf-8 -*-
"""
@File    : DownloadBooks.py
@Time    : 2022/2/18 15:04
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
import selenium
from USER_AGENT import UA_list
import random
import json
from lxml import etree
import os
from selenium import webdriver
import time


class BookSpider:
    def __init__(self, keyword, num):
        self.keyword = keyword
        self.num = num
        self.base_url = 'https://ca1lib.org'
        self.book_url = '/s/{}?page={}'
        self.headers = {
            'user-agent': random.choice(UA_list)
        }
        self.session = requests.session()
        mkdir('./{}'.format(self.keyword))
        with open('proxies.txt', 'r') as file:
            self.proxy_list = file.readlines()
    
    def parse_init_page(self):
        print('开始下载初始界面')
        item_num = 0
        all_book_list = []
        for i in range(1, self.num + 1):
            try:
                my_proxies = {"http": "socks5h://{}".format(self.proxy_list[0]), "https": "socks5h://{}".format(self.proxy_list[0])}
            except IndexError:
                print('代理已经用完，请重新获得最新代理。完成后请输入w')
                s = input()
                if s == 'w':
                    with open('proxies.txt', 'r') as file:
                        self.proxy_list.extend(file.readlines())
                        
            content = self.session.get(
                self.base_url +
                self.book_url.format(
                    self.keyword,
                    i),
                headers=self.headers,proxies=my_proxies).content.decode('utf-8')
            selector = etree.HTML(content)
            url_list = selector.xpath(
                '//div[@itemtype="http://schema.org/Book"]')
            # print(len(url_list))
            for xpath in url_list:
                temp = {}
                book_name = xpath.xpath('.//h3/a/text()')[0]
                book_url = xpath.xpath('.//h3/a/@href')[0]
                try:
                    book_publisher = xpath.xpath(
                        './/a[@title="Publisher"]/text()')[0]
                except BaseException:
                    book_publisher = 'Not Found'
                book_type = xpath.xpath(
                    './/div[@class="bookProperty property__file"]/div[2]/text()')[0].split(',')[0]
                
                temp['item_num'] = item_num
                temp['name'] = book_name
                temp['book_url'] = self.base_url + book_url
                temp['type'] = book_type.split(',')[0]
                temp['publisher'] = book_publisher
                
                all_book_list.append(temp)
                item_num += 1
                # print(temp)
            print('第{}页下载完成'.format(i))
        with open('./{}/BookList.json'.format(self.keyword), 'w', encoding='utf-8') as file:
            json.dump(all_book_list, file, indent=4, ensure_ascii=False)
            print('初始界面下载完毕')
        
        return all_book_list
    
    def init_options(self,dir_num):
        options = webdriver.ChromeOptions()
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.popups": 0,
            "download.default_directory": "C:\\Users\\29745\\PycharmProjects\\spider\\下载书本\\{}\\{}".format(
                self.keyword,
                dir_num)}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--user-agent={}'.format(random.choice(UA_list)))
        # options.add_argument('--headless')

        try:
            options.add_argument(
                ' proxy-server=socks5://' +
                self.proxy_list[0].replace(
                    '\n',
                    ''))
        except IndexError:
            
            print('代理已经用完，请重新获得最新代理。完成后请输入w')
            s = input()
            if s == 'w':
                with open('proxies.txt', 'r') as file:
                    self.proxy_list.extend(file.readlines())
        return options
    
    def parse_detail_page(self, url, dir_num, name):
        # 防止出现无法连接的错误
        try:
            options = self.init_options(dir_num)
            # 设置等待时间不超过30s
            browser = webdriver.Chrome(options=options)
            browser.set_page_load_timeout(30)
            
            # 如果加载时间超过最长等待时间，判定为IP无效。此时重新执行这个模块
            try:
                browser.get(url)
                # time.sleep(100)
            except selenium.common.exceptions.TimeoutException:
                print('代理:{} 无效'.format(self.proxy_list[0].replace('\n','')))
                print('网站无法访问')
                del (self.proxy_list[0])
                with open('proxies.txt', 'w') as file:
                    for proxy in self.proxy_list:
                        file.write(proxy)
                browser.quit()
                self.parse_detail_page(url, dir_num, name)
            
            # 获得封面的url
            cover = browser.find_element_by_xpath(
                '//div[@class="z-book-cover"]/img')
            cover_url = cover.get_attribute('src')
            
            # 创建新的文件夹
            mkdir('./{}/{}'.format(self.keyword, dir_num))
            
            # 下载图片
            with open('./{}/{}/cover.{}'.format(self.keyword, dir_num, cover_url.split('.')[-1]), 'wb') as file:
                file.write(
                    self.session.get(
                        cover_url,
                        headers=self.headers).content)
                print('{} 图片下载完成'.format(name))
            
            # 获得按钮下载的连接
            download_part = browser.find_element_by_xpath(
                '//a[@class="btn btn-primary dlButton addDownloadedBook"]')
            download_url = download_part.get_attribute('href')
            print(download_url)
            time.sleep(5)
            
            # 尝试点击下载按钮
            download_button = browser.find_element_by_xpath(
                '//a[@class="btn btn-primary dlButton addDownloadedBook"]')
            start_time = time.time()
            try:
                download_button.click()
                time.sleep(1)
                
                # 获得点击下载之后的url。与之前的相比较。如果不同，说明此时的IP已经无效
                if browser.current_url == download_url:
                    print('代理:{} 无效'.format(self.proxy_list[0].replace('\n', '')))
                    print('此代理下载次数以用完')
                    time.sleep(1)
                    del (self.proxy_list[0])
                    with open('proxies.txt', 'w') as file:
                        for proxy in self.proxy_list:
                            file.write(proxy)
                    browser.quit()
                    self.parse_detail_page(url, dir_num, name)
                
                else:
                    # 查找是否下载完成。使用os模块判断后缀名。如果未完成，继续下载。否则，等待下载完成
                    print('代理有效')
                    while True:
                        file_dir,_ = file_name("C:/Users/29745/PycharmProjects/spider/下载书本/{}/{}".format(self.keyword, dir_num))
                        for fname in file_dir:
                            if 'cover' in fname:
                                file_dir.remove(fname)
                        
                        # 没有后缀，并且只有一个文件（除照片），说明已经下载完毕
                        try:
                            now_time = time.time()
                            if now_time - start_time > 360:
                                for book_file in file_dir:
                                    if 'crdownload' in file_dir[0]:
                                        os.remove("C:/Users/29745/PycharmProjects/spider/下载书本/{}/{}/{}".format(self.keyword,
                                                                                                           dir_num,
                                                                                                           book_file))
                                print('下载失败')
                                break
                            if not 'crdownload' in file_dir[0] and len(file_dir)==1:
                                browser.quit()
                                os.rename("C:/Users/29745/PycharmProjects/spider/下载书本/{}/{}/{}".format(self.keyword, dir_num,file_dir[0]),"C:/Users/29745/PycharmProjects/spider/下载书本/{}/{}/{}".format(self.keyword, dir_num,file_dir[0].replace('(z-lib.org)','')))
                                print('书籍{}下载完成'.format(name))
                                break
                            elif len(file_dir) > 1:
                                browser.quit()
                                print('重复下载')
                                break
                            else:
                                time.sleep(10)
                        # 说明并未下载，及下载失败
                        except IndexError:
                            print('代理下载失败。进行下一次下载')
                            del(self.proxy_list[0])
                            browser.quit()
                            # time.sleep(1000)
                            self.parse_detail_page(url,dir_num,name)
            # 如果点击下载长时间没有回应
            except selenium.common.exceptions.TimeoutException:
                print('代理:{} 无效'.format(self.proxy_list[0].replace('\n','')))
                del (self.proxy_list[0])
                with open('proxies.txt', 'w') as file:
                    for proxy in self.proxy_list:
                        file.write(proxy)
                browser.quit()
                self.parse_detail_page(url, dir_num, name)
        except Exception as e:
            try:
                browser.quit()
            except:
                pass
            time.sleep(random.random() *10)
            self.parse_detail_page(url,dir_num,name)
            
    def run(self):
        book_file, dirs = file_name("C:/Users/29745/PycharmProjects/spider/下载书本/{}".format(self.keyword))
        if len(book_file) == 0:
            book_list = self.parse_init_page()
        else:
            with open('./{}/BookList.json'.format(self.keyword), 'r', encoding='utf-8') as file:
                book_list = json.load(file)
                print('数据加载完成')

        for i in dirs:
            file,_ = file_name("C:/Users/29745/PycharmProjects/spider/下载书本/{}/{}".format(self.keyword,i))
            if len(file) <2:
                dirs.remove(i)
                
        for i in range(len(dirs),len(book_list)):
            self.parse_detail_page(
                book_list[i]['book_url'], i, book_list[i]['name'])


def mkdir(path):
    folder = os.path.exists(path)
    
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def file_name(file_dir):
    for abs_path, dirs, files in os.walk(file_dir):
        # 当前路径下所有非目录子文件
        return files,dirs


if __name__ == '__main__':
    spider = BookSpider('Python', 5)
    spider.run()
    # spider.parse_init_page()
    # mkdir('./测:][*-s')
    # file_name('./Java/0')
