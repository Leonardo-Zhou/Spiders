# -*- coding: utf-8 -*-
"""
@File    : DownloadBooksNew.py
@Time    : 2022/2/19 20:50
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


def make_dir(path):
    """
    判断是否存在某个文件夹。如果不存在，则创建
    :param path: 绝对路径
    :return: None
    """
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)


def file_name(file_dir):
    """
    用于获得某路径下的文件/文件夹/该路径的绝对路径
    :param file_dir: 绝对路径
    :return: 文件的绝对路径，该路径下文件夹名称，该路径下文件名称
    """
    for abs_path, dirs, files in os.walk(file_dir):
        # 当前路径下所有非目录子文件
        return abs_path, dirs, files


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
        make_dir('./{}'.format(self.keyword))
        with open('proxies.txt', 'r') as file:
            self.proxy_list = file.readlines()
    
    def init_options(self, dir_num):
        """
        用于初始化chrome的选项
        :param dir_num: 该书籍的固定编号
        :return:
        """
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.popups": 0,
            "download.default_directory": "C:\\Users\\29745\\PycharmProjects\\spider\\下载书本\\{}\\{}".format(
                self.keyword,
                dir_num)}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--user-agent={}'.format(random.choice(UA_list)))
        
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
    
    def del_useless_proxy(self):
        del (self.proxy_list[0])
        with open('proxies.txt', 'w') as file:
            for proxy in self.proxy_list:
                file.write(proxy)
    
    def parse_init_page(self):
        """
        下载搜索界面
        :return: 形式为[{'item_num':0, 'name':'', 'book_url':'', 'type':'', 'publisher':''},{}]
        """
        print('开始下载初始界面')
        item_num = 0
        all_book_list = []
        for i in range(1, self.num + 1):
            try:
                my_proxies = {"http": "socks5h://{}".format(self.proxy_list[0]),
                              "https": "socks5h://{}".format(self.proxy_list[0])}
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
                headers=self.headers, proxies=my_proxies).content.decode('utf-8')
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
    
    def del_repeated_book(self, serial_num, file_temp_name):
        print('存在重复文件{}'.format(file_temp_name))
        os.remove('./{}/{}/{}'.format(self.keyword, serial_num, file_temp_name))
        print('重复文件已删除')
        
    
    def parse_detail_page(self, url, serial_num, name):
        try:
            print('尝试下载 {}'.format(name))
            options = self.init_options(serial_num)
            
            # 设置等待时间不超过30s
            browser = webdriver.Chrome(options=options)
            browser.set_page_load_timeout(30)
            
            browser.get(url)
            
            # 获得封面的url
            cover = browser.find_element_by_xpath(
                '//div[@class="z-book-cover"]/img')
            cover_url = cover.get_attribute('src')
            print('网页成功访问')
            
            # 创建新的文件夹
            make_dir('./{}/{}'.format(self.keyword, serial_num))
            
            abs_path, dirs, files = file_name('./{}/{}'.format(self.keyword, serial_num))
            
            # 下载图片
            if not 'cover.{}'.format(cover_url.split('.')[-1]) in files:
                with open('./{}/{}/cover.{}'.format(self.keyword, serial_num, cover_url.split('.')[-1]), 'wb') as file:
                    file.write(
                        self.session.get(
                            cover_url,
                            headers=self.headers).content)
                    print('{} 图片下载完成'.format(name))
            else:
                print('图片已下载')
            
            # 获得按钮下载的连接
            download_part = browser.find_element_by_xpath(
                '//a[@class="btn btn-primary dlButton addDownloadedBook"]')
            download_url = download_part.get_attribute('href')
            
            time.sleep(3)
            
            # 尝试点击下载按钮
            download_button = browser.find_element_by_xpath(
                '//a[@class="btn btn-primary dlButton addDownloadedBook"]')
            # 获得当前下载时间。如果很久未下载完成，说明可能下载失败
            start_time = time.time()
            
            download_button.click()
            
            # 获得点击下载之后的url。与之前的相比较。如果不同，说明此时的IP已经无效
            if browser.current_url == download_url:
                raise DownloadsExhaustedError
            else:
                print('开始下载书籍')
                while True:
                    time.sleep(10)
                    abs_path, dirs, files = file_name('./{}/{}'.format(self.keyword, serial_num))
                    files.remove('cover.{}'.format(cover_url.split('.')[-1]))
                    now_time = time.time()
                    # 持续下载时常超过360s，说明下载失败
                    if now_time - start_time > 360:
                        raise DownloadTimeoutError
                    else:
                        for book_file_name in files:
                            if not 'crdownload' in book_file_name:
                                print('{} 下载成功'.format(name))
                                new_name = book_file_name.replace('(z-lib.org)', '')
                                for book_num in range(1,len(files)+1):
                                    try:
                                        new_name.replace('({})'.format(book_num),'')
                                    except:
                                        pass
                                os.rename('./{}/{}/{}'.format(self.keyword, serial_num, files[0]),
                                          './{}/{}/{}'.format(self.keyword, serial_num,
                                                              new_name))
                                browser.quit()
                                _, _, files = file_name('./{}/{}'.format(self.keyword, serial_num))
                                for download_temp_name in files:
                                    if 'crdownload' in download_temp_name:
                                        self.del_repeated_book(serial_num, download_temp_name)
                                return None
                            #     if book_file_name == files[-1]:
                            #         pass
                            #     else:
                            #         for temp_num in range(files.index(book_file_name),len(files)):
                            #             print('存在重复文件')
                            #             os.remove('./{}/{}/{}'.format(self.keyword, serial_num, book_file_name))
                            #             print('删除完成')
                            #     break
                            # else:
                            #     print('存在重复文件')
                            #     os.remove('./{}/{}/{}'.format(self.keyword, serial_num, book_file_name))
                            #     print('删除完成')
                            #     continue
                            else:
                                continue

        # 出现timeout错误，说明未能加载进网页
        except selenium.common.exceptions.TimeoutException:
            print('proxy {} 无效，网页无法访问'.format(self.proxy_list[0].replace('\n', '')))
            try:
                browser.quit()
            except:
                pass
            self.del_useless_proxy()
            self.parse_detail_page(url, serial_num, name)
        
        # 自定义下载次数用尽error
        except DownloadsExhaustedError:
            print('proxy {} 下载次数用尽'.format(self.proxy_list[0].replace('\n', '')))
            try:
                browser.quit()
            except:
                pass
            self.del_useless_proxy()
            self.parse_detail_page(url, serial_num, name)
        
        # 自定义下载失败error
        except DownloadTimeoutError:
            print('proxy {} 下载文件失败'.format(self.proxy_list[0].replace('\n', '')))
            try:
                browser.quit()
            except:
                pass
            self.del_useless_proxy()
            self.parse_detail_page(url, serial_num, name)
        
        # 出现任何差错，直接重新开始一次
        except:
            try:
                browser.quit()
            except:
                pass
            self.del_useless_proxy()
            self.parse_detail_page(url, serial_num, name)
    
    def run(self):
        _, dirs, files = file_name('./{}'.format(self.keyword))
        if len(files) > 0:
            with open('./{}/BookList.json'.format(self.keyword), 'r', encoding='utf-8') as file:
                book_list = json.load(file)
                print('数据加载完成')
        else:
            book_list = self.parse_init_page()
            
        for folder in dirs:
            _,_,f = file_name('./{}/{}'.format(self.keyword,folder))
            if len(f) == 2:
                for book_in_list in book_list:
                    if book_in_list['item_num']==int(folder):
                        book_list.remove(book_in_list)
                        break

        
        for book_detail in book_list:
            self.parse_detail_page(book_detail['book_url'],book_detail['item_num'],book_detail['name'])


class DownloadsExhaustedError(Exception):
    pass


class DownloadTimeoutError(Exception):
    pass


if __name__ == '__main__':
    spider = BookSpider('Python',5)
    spider.run()
