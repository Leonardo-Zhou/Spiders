
# -*- coding: utf-8 -*-
import time

import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import re


class GetIpData():
    """爬取50页国内高匿代理IP"""
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    base_url1 = 'https://www.kuaidaili.com/free/inha/'
    base_url2 = 'http://www.xsdaili.cn/dayProxy/ip/'
    check_url = 'https://ca1lib.org/s/Java?'
    json_data = []

    def get_url_html(self, url):
        """请求页面html"""
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ("User-Agent",
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]

        return opener.open(url).read().decode('utf-8')

    def check_ip(self, ip_info):
        """测试IP地址是否有效"""
        ip_url = ip_info['ip'] + ':' + str(ip_info['port'])
        res = False
        try:
            proxy = urllib.request.ProxyHandler({'HTTP': ip_url})
            opener = urllib.request.build_opener(proxy)
            opener.addheaders = [
                ("User-Agent",
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]
            request = opener.open(self.check_url)
            if request.status == 200:
                res = True
        except Exception as error_info:
            res = False
        return res

    def run_1(self):
        """执行入口"""
        page_list = range(1, 10)
        with open("JD/ip.json", "w") as write_file:
            for page in page_list:
                time.sleep(0.5)
                # 分页爬取数据
                print('开始爬取第' + str(page) + '页IP数据')
                ip_url = self.base_url1 + str(page) + '/'
                html = self.get_url_html(ip_url)
                soup = BeautifulSoup(html, 'html.parser')
                # IP列表
                ip_soup = soup.find_all('tr')[1:-1]
                for ip_tr in ip_soup:
                    ip_address = ip_tr.find(attrs={"data-title": "IP"}).string
                    ip_port = ip_tr.find(attrs={'data-title': 'PORT'}).string
                    info = {'ip': ip_address, 'port': ip_port}
                    # 先校验一下IP的有效性再存储
                    check_res = self.check_ip(info)
                    if check_res:
                        print('IP有效：', info)
                        proxy = ip_address + ':' + ip_port
                        self.json_data.append(proxy)
                    else:
                        print('IP无效：', info)
            json.dump(self.json_data, write_file)

    def run_2(self):
        """执行入口"""
        page_list = range(3071, 3061, -1)
        with open("ip.json", "a") as write_file:
            for page in page_list:
                time.sleep(0.5)
                # 分页爬取数据
                print('开始爬取第' + str(page) + '页IP数据')
                ip_url = self.base_url2 + str(page) + '.html'
                html = self.get_url_html(ip_url)
                soup = BeautifulSoup(html, 'html.parser')
                # IP列表
                ip_soup = soup.find(class_="cont").text
                list_temp = list()
                temp_list = ip_soup.replace('\n', '').split(' ')
                temp_list = list(filter(None, temp_list))
                print(temp_list)
                for i in temp_list:
                    if i[0] == '1':
                        temp = i.split('#')
                        if temp[0][-1] != 'S':
                            list_temp.append(temp[0][0:-5])

                for ip_tr in list_temp:
                    ip_address, ip_port = ip_tr.split(':')
                    info = {'ip': ip_address, 'port': ip_port}
                    # 先校验一下IP的有效性再存储
                    check_res = self.check_ip(info)
                    if check_res:
                        print('IP有效：', info)
                        proxy = ip_address + ':' + ip_port
                        self.json_data.append(proxy)
                    else:
                        print('IP无效：', info)
            json.dump(self.json_data, write_file)

    def check_local_ip(self):
        with open('IP.txt', 'r') as file:
            IP_list = file.readlines()
        for ip in IP_list:
            ip_dict = dict()
            ip_dict['ip'] = ip.split(':')[0]
            ip_dict['port'] = ip.split(':')[1].replace('\n', '')
            print(ip.replace('\n', '  ') + str(self.check_ip(ip_dict)))


# 程序主入口
if __name__ == '__main__':
    # 实例化
    ip = GetIpData()
    # 执行脚本
    # ip.run_1()
    # ip.run_2()
    ip.check_local_ip()
