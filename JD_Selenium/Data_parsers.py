# -*- coding: utf-8 -*-
"""
@File    : Data_parsers.py
@Time    : 2021/12/27 20:26
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

from pymongo import MongoClient
from lxml.etree import HTML
import re
import json
from BlockWord import BLOCKWORDS
from Tools import Tools
import string


class parser:
    def __init__(self):
        # self.pat_para = re.compile(
        #     '(.*\n)*.*skuid: (\\d*)(.*\n)*.*skuMarkJson: ({(.*)*?})(.*\n)*.*name: (\'.*\')('
        #     '.*\n)*.*colorSize: (\\[{.*}*\\])')
        self.id_pattern = re.compile('(.*\n)*.*skuid: (\\d*)')
        self.json_pattern = re.compile('(.*\n)*.*skuMarkJson: ({(.*)*?})')
        self.name_pattern = re.compile('(.*\n)*.*name: (\'.*\')')
        self.colorSize_pattern = re.compile('(.*\n)*.*colorSize: (\\[{.*?}*\\])')
        self.tools = Tools()
        # self.db = MongoClient()['京东'][keyword]
    
    def parse_page(self, content, first_page=False):
        """
        
        :param content: 以解码的页面content
        :param first_page: 判断是否是在搜索后的第一页
        :param sku_list: 形如[{'skuId': 100011579191, '处理器或显卡': 'R9000X/RTX3060/R7/165Hz 2.5K屏'}, {'skuId': 100011527449, '处理器或显卡': 'R9000P/RTX3050Ti/R7/165Hz 2.5k'}]
        :return:
        """
        
        sku_id = json.loads(re.match(self.id_pattern,content)[2])
        '''
        sku_mark_json格式：
        {'isxg': False,
        'isJDexpress': False,
        'isrecyclebag': False,
        'isSds': False,
        'isSopJSOLTag': False,
        'isyy': False,
        'isPOPDistribution': False,
        'isSopUseSelfStock': False,
        'isGlobalPurchase': False,
        'NosendWMS': False,
        'isOripack': False,
        'ispt': False,
        'unused': False,
        'pg': False,
        'isSopWareService': False,
        'isTimeMark': False,
        'presale': False}
        '''
        sku_mark_json = json.loads(re.match(self.json_pattern,content)[2])
        name = re.match(self.name_pattern,content)[2]
        if first_page:
            sku_list = json.loads(re.match(self.colorSize_pattern,content)[2])
        
        # 将商品列表中的已经爬取过的部分删除
            for i in range(len(sku_list)):
                if sku_list[i]['skuId'] == sku_id:
                    sku_list.pop(i)
                    break
        else:
            sku_list = []
        # print(sku_list)
        parameter,price = self.parse_detailed(content, sku_id)
        
        detail_info = {
            "商品标题": self.tools.delete_block_words(name).replace("'",''),
            "预售": sku_mark_json['presale'],
            "价格": price,
            "详细参数": parameter,
            "网址": 'https://item.jd.com/{}.html'.format(sku_id),
        }
        # print(detail_info)
        # print('name:{}'.format(self.tools.delete_block_words(name)))
        return detail_info, sku_list
    
    def parse_detailed(self, content, sku_id):
        selector = HTML(content)

        information = {}
        price = {}
        
        # 获得价格
        # 正常价格
        p_price = int(self.tools.delete_not_ascii(selector.xpath('//span[@class="price J-p-%s"]/text()' % sku_id)[0]).split('.')[0])
        # 学生价格
        try:
            student_price = int(self.tools.delete_not_ascii(selector.xpath('//span[@class="student-price"]/em/text()')[0]).split('.')[0])
        except:
            student_price = None
        #  活动价格
        try:
            active_price = int(self.tools.delete_not_ascii(selector.xpath('//div[@class="activity-price"]/span/text()')[0]).split('.')[0])
        except:
            active_price = None
            
        price["正常价格"] = p_price
        price["学生价"] = student_price
        price["活动价"] = active_price

        # 获得商品介绍部分内容
        xpath_list = selector.xpath('//ul[@class="parameter2 p-parameter-list"]/li')

        temp = {}
        for i in xpath_list:
            tmp = i.xpath('./text()')[0]
            temp_list = tmp.split('：') if '：' in tmp else tmp.split(':')
            temp[temp_list[0]] = temp_list[1]

        information["商品介绍"] = temp
        # print(temp)

        # 获得详细参数
        xpath_list = selector.xpath('//div[@class="Ptable"]/div')
        temp1 = dict()
        for i in xpath_list:
            # 获得参数标题
            title = i.xpath('./h3/text()')[0]
            temp = dict()
            for j in i.xpath('./dl/dl'):
                # 在获得参数时如果碰到有为空格行的，判断并且正确选择
                for q in j.xpath('./dt'):
                    sub_title = q.xpath('./text()')[0]
                    if sub_title.replace('\n', '').split():
                        break
                for q in j.xpath('./dd'):
                    sub_info = q.xpath('./text()')[0]
                    if sub_info.replace('\n', '').split():
                        break
                temp[sub_title] = sub_info
            temp1[title] = temp
        information['规格与包装'] = temp1
        
        return information, price
    
    def parse_init_page(self, content):
        """
        用于解析搜索页面，获得各个商品类的url
        :param content: 搜索页面的content
        :return: 商品类url列表
        """
        selector = HTML(content)
        xpath_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
        commodity_url_list = []
        for i in xpath_list[1:]:
            commodity_url_list.append('https:' + i.xpath('./div/div[1]/a/@href')[0])
        
        return commodity_url_list


    
if __name__ == '__main__':
    with open('./测试文件/test.html', 'rb') as file:
        con = file.read().decode('utf-8')

    with open('./测试文件/init_page.html', 'rb') as file:
        cont = file.read().decode('utf-8')
    par = parser()
    # infor, price = par.parse_detailed(con, '100014794825')
    # print(infor)
    detail_info, sku_list = par.parse_page(con,True)
    print(detail_info)
    # par.parse_init_page(cont)
    
