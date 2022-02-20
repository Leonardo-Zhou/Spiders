# -*- coding: utf-8 -*-
"""
@File    : JDSpider.py
@Time    : 2021/12/26 15:11
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
import re
from pymongo import MongoClient
from lxml import etree
import random
from USER_AGENT import UA_list
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def options():
    """
    :return: 浏览器设置
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--user-agent={}'.format(random.choice(UA_list)))
    prefs = {"download.default_directory": "NUL", "download.prompt_for_download": False, "profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    return chrome_options


class spider:
    def __init__(self, n, keyword):
        self.keyword = keyword
        self.base_url = 'https://search.jd.com/Search?keyword={}&page='.format(
            self.keyword)
        self.detail_base = 'https://item.jd.com/{}.html'
        self.db = MongoClient()['京东'][self.keyword]
        self.pattern = re.compile('(.*\n)*.*colorSize: (\[\{.*\}*\])')
        self.detail_information_base = 'https://item-soa.jd.com/getWareBusiness?skuId={}&cat=670%2C671%2C673&area=1_72_2799_0'
        self.n = n
        self.browser = webdriver.Chrome(chrome_options=options())

    # 搜索页面
    def parse_initial(self, page):
        if page < self.n+1:
            url = self.base_url + str(page)
            headers = {
                'User-Agent': random.choice(UA_list)
            }
            content = requests.get(
                url, headers=headers).content.decode('utf-8')
            selector = etree.HTML(content)
            temp = selector.xpath('//*[@id="J_goodsList"]'
                                  '/ul/li')[1:]
            if not temp:
                self.parse_initial(page)
            else:
                for i in temp[1:]:
                    # 获得初始界面的每个对应的sku值
                    if i.xpath('./@data-spu') == ['']:
                        pass
                    else:
                        sku = i.xpath('./@data-sku')[0]
                        self.parse(self.detail_base.format(sku),temp.index(i))
                page += 1
                print('第{}页完成爬取'.format(page-1))
        else:
            pass

    # 详细界面初,提取初始界面中的所有sku_id
    def parse(self, url, num):
        # time.sleep(random.random()*3)
        headers = {
            'User-Agent': random.choice(UA_list)
        }
        content = requests.get(
            url=url, headers=headers).content.decode('utf-8')
        if len(content) < 1000:
            self.parse(url,num)
        else:
            # try:
            # 用来匹配skuid的值
            tempp = re.match(self.pattern, content)
            # print(content)
            
            # print(url)
            selector = etree.HTML(content)
            initial_name = selector.xpath('//title/text()')[0]
            try:
                tmp = tempp[2]
                tmp = tmp.replace('\'','\"')
                temp_json = json.loads(tmp)
                # 用来获取商店页面的title名称
            except Exception as e:
                pattern_temp = re.compile('https://item.jd.com/(\d*)\.html')
                temp_json = [{'skuId': re.match(pattern_temp,url)[1],
                              '名称': ' '.join(selector.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')[0].replace('\n','').split())}]
            for sku in temp_json:
                self.parse_details(sku.pop('skuId'), ' / '.join(sku.values()), initial_name)
            print('第{}个商品类已经完成爬取'.format(num))
                
    # 商品详情界面解析
    def parse_details(self, sku_id, name, initial_name):
        '''
        
        :param sku_id: 商品独有的id
        :param name: 商品的各项性能/指标等可供选择的选项的标签
        :param initial_name: 商品界面上公用的title
        :return: 商品的详细信息
        '''
        headers = {
            'user-agent': random.choice(UA_list),
            'cookies':
            'token=4131365db76d520ca1c86d9e9efc2921,1,911450; __jda=122270672.16406100941401313025812.1640610094.1640610094.1640610094.1; __jdb=122270672.1.16406100941401313025812|1.1640610094; __jdc=122270672; __jdv=122270672|direct|-|none|-|1640610094141; shshshfp=827362b9914b13f6c56b35ac15d8d1e5; shshshfpa=9fd957a5-c958-3df4-765f-1ab8ce22d2e9-1640610095; shshshsID=c5276410801d88f6d0cbdac262afab82_1_1640610095166; shshshfpb=eutNDpqabjePWjn41Zxq3gQ==; areaId=15; ip_cityCode=1262; ipLoc-djd=15-1262-1267-56327; 3AB9D23F7A4B3C9B=ZYW2JNUUDVQPM4OHDMCDJK2DCKZPUTOWMQIEMIHGM64Z2UMFKIDED6UF6EIHVYXSXYJ42O6KAJ4HPIP75PFUYSVPO4'
        }
        # 使用不同的IP
        with open('ip.json', 'r') as file:
            proxies = json.load(file)
            ip_address = random.choice(proxies)
            # ip_address = proxies[0]
            # proxy = {
            #     "http": 'socks5://zhima:zhima@{}:{}/'.format(ip_address['ip'], ip_address['port']),
            #     "https": 'socks5://zhima:zhima@{}:{}/'.format(ip_address['ip'], ip_address['port'])
            # }
            # print(proxies)
            
        url = self.detail_information_base.format(sku_id)
        try:
            # con = requests.get(
            #     url,
            #     # proxies=proxy,
            #     headers=headers
            #     )
            # content = con.content
            # with open('a.html','wb') as file:
            #     file.write(content)
            # print(content)
            print(url)
            self.browser.get(url)
            time.sleep(random.random() *5)
            content = self.browser.find_element_by_xpath('/html/body/pre').text
            
            try:
                temp_json = json.loads(content)
                price = int(temp_json['price']['p'].split('.')[0])
                original_price = int(temp_json['price']['op'].split('.')[0])
                shop_info = temp_json['shopInfo']['shop']
                shop_name = shop_info['name']
    
                # 获得商店的详细情况
                try:
                    after_sale_score = shop_info['afterSaleScore']
                except BaseException:
                    after_sale_score = 'Not Found'
    
                try:
                    logistics_score = shop_info['logisticsScore']
                except BaseException:
                    logistics_score = 'Not Found'
    
                try:
                    score_rank_rate_grade = shop_info['scoreRankRateGrade']
                except BaseException:
                    score_rank_rate_grade = 'Not Found'
    
                try:
                    delivery_place = temp_json['deliveryPlace']
                except BaseException:
                    delivery_place = 'Not Found'
    
                # 促销情况
                try:
                    promotions_list = temp_json['shopInfo']['shop']['promotions']
                    promotions = ' / '.join([i['name'] for i in promotions_list])
                except Exception as e:
                    promotions = 'No'
    
                # 判断是否有货
                stock = temp_json['stockInfo']['stockDesc']
                pat = re.compile('<strong>(.*)</strong>')
                stock_information = re.match(pat, stock)[1]
    
                # 判断是否能分期
                # pat = re.compile('{.*"act.":(.),.*')
                staging_details = []
                try:
                    judge_temp = temp_json['baitiaoPlanShowResVo']
                    judge = json.loads(judge_temp)['act']
                    if judge:
                        staging_details_temp = temp_json['whiteBarInfo']['planInfos']
                        for i in staging_details_temp:
                            staging_main = i['mainTitle']
                            extra_money = i['total'] - price
                            rate = i['rate']
                            staging_details.append('分期情况：{}，额外支付：{}，费率：{}'.format(staging_main, extra_money, rate))
                    else:
                        staging_details.append('No')
                except:
                    # print(sku_id)
                    staging_details.append('No')
    
                # 详细情况
                name = self.judge_name(initial_name, name)
                product = {
                    '型号': name,
                    '价格': price,
                    '原价': original_price,
                    '货源': stock_information,
                    '活动': promotions,
                    '分期情况': staging_details if not len(staging_details) == 1 else 'No',
                    '商店': {
                        '名称': shop_name,
                        '售后': after_sale_score,
                        '物流': logistics_score,
                        '综合': score_rank_rate_grade,
                        '发货地': delivery_place},
                    '地址': self.detail_base.format(sku_id)
                }
                self.store_data(product)

            except BaseException as e:
                print(1)
                print(e)
                print(content)
                # time.sleep(random.random() * 2)
                # proxies.remove(ip_address)
                # with open('ip.json','w') as file:
                #     file.write(json.dumps(proxies))
                self.parse_details(name, sku_id, initial_name)
        except Exception as e:
            print(e)
            self.parse_details(sku_id,name,initial_name)
            
        
    
    # 判断名字
    def judge_name(self,initial_name,name_type):
        '''
        
        :param initial_name: 商品界面上的title。在此处将对其进行分词
        :param name_type: 分析过程中商品的各种硬件情况
        :return: 在数据库中显示的名称,name
        '''
        name_list = self.keyword.split(' ')
        flag = False
        # 如果flag=True，则说明参数配置选项中包含了我所需要的名称，则不用进行后面的活动
        for i in name_list:
            if i in name_type or i.upper() in name_type:
                name = name_type
                return name
        
        if not flag:
            title_split = initial_name.replace('·',' ').split(' ')
            # print(title_split)
            
            for i in name_list:
                for j in title_split:
                    if i.upper() in j or i in j:
                        name = j + ' ' +name_type
                        return name
        return name_type

    def store_data(self,data):
        self.db.insert_one(data)
        
    
    
if __name__ == '__main__':
    # n = int(input('需要爬取的页数：'))
    # keyword = input('关键词：')
    n = 2
    keyword = '联想 r9000p'
    s = spider(n,keyword)
    s.parse_initial(1)
