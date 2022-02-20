# -*- coding: utf-8 -*-
"""
@File    : use_re.py
@Time    : 2021/12/26 14:26
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import re

# pat = re.compile('{.*"act.":(.),.*')
# data = r"{\"act\":0,\"bp\":1,\"creditStatus\":1,\"isAva\":false,\"isBtUser\":true,\"isDiscountAll\":false,\"isFull\":false,\"isItemAva\":true,\"isLogin\":true,\"isScc\":false,\"isShopAva\":true,\"isSkuAva\":true,\"key\":\"0DDD4340F5540A836C8C0CCF9639B2B1\",\"marketingText\":\"\",\"noAvaInfo\":\"\",\"planInfos\":[{\"curTotal\":9577.00,\"fee\":0.00,\"firstPay\":9577.00,\"firstRepayDate\":\"2022-01-26\",\"isDiscount\":false,\"laterPay\":9577.00,\"maxDiscount\":true,\"plan\":1,\"planFee\":0.00,\"rate\":0.00,\"total\":9577.00},{\"curTotal\":3259.38,\"fee\":201.12,\"firstPay\":3259.37,\"firstRepayDate\":\"2022-01-26\",\"isDiscount\":false,\"laterPay\":3259.38,\"maxDiscount\":false,\"plan\":3,\"planFee\":67.04,\"rate\":0.70,\"total\":9778.12},{\"curTotal\":1663.19,\"fee\":402.24,\"firstPay\":1663.21,\"firstRepayDate\":\"2022-01-26\",\"isDiscount\":false,\"laterPay\":1663.19,\"maxDiscount\":false,\"plan\":6,\"planFee\":67.04,\"rate\":0.70,\"total\":9979.24},{\"curTotal\":865.16,\"fee\":804.48,\"firstPay\":865.12,\"firstRepayDate\":\"2022-01-26\",\"isDiscount\":false,\"laterPay\":865.16,\"maxDiscount\":false,\"plan\":12,\"planFee\":67.04,\"rate\":0.70,\"total\":10381.48},{\"curTotal\":466.12,\"fee\":1608.96,\"firstPay\":466.08,\"firstRepayDate\":\"2022-01-26\",\"isDiscount\":false,\"laterPay\":466.12,\"maxDiscount\":false,\"plan\":24,\"planFee\":67.04,\"rate\":0.70,\"total\":11185.96}],\"propMarketText\":\"\",\"result\":{\"code\":\"00000\",\"info\":\"success\",\"success\":true},\"sccBt\":false,\"ver\":\"1\"}"
# 
# print(re.match(pat,data)[1])
# with open('c.html','rb') as file:
#     temp = file.read().decode('utf-8')
#     # for i in temp:
#     #     a = i.decode('utf-8')
#     #     b = re.match(pattern, a)
#     #     if b:
#     #         print(b[1])
#     print(re.match(pattern,temp)[2])

# with open('t.html','rb') as file:
#     content = file.read().decode('utf-8')
#     
# pattern = re.compile('.*<title>(.*)</title>.*')
# 
# print(re.match(pattern,content))

pattern_temp = re.compile('https://item.jd.com/(\d*)\.html')
url = 'https://item.jd.com/100010793473.html'

print(re.match(pattern_temp,url)[1])