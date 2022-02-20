# -*- coding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/12/26 15:46
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import requests
from USER_AGENT import UA_list
import random
import json
#

url = 'https://item.jd.com/10026693132819.html'
headers = {
	# 'cookie':
	# '__jdv=76161171|direct|-|none|-|1640504396269; __jdu=16405043962681952968723; areaId=15; ipLoc-djd=15-1158-0-0; PCSYCityID=CN_330000_330200_0; shshshfp=69f73832f14665286beeb0f263bdabb6; shshshfpa=571e99de-82c0-77d7-88aa-74cb7c8c6f54-1640504398; shshshfpb=pltUjAThyNuMlqqkgl8oMow==; user-key=84788049-3203-404d-837d-72104fbaad51; TrackID=1QBp_jlPTwc4nTT6bdpu9YAZQJGKt2lHmbQZdfKvp7el6VOjaQ0rKb3YxIaJkKmYDJNNPZj9sanYsukUwYFLLtg-w384X-AfyN2VtT46Uu7s; pinId=lfRwDzFfieBCdX0Esb2nqg; pin=leonardo_zhou; unick=leonardo_zhouZRi; ceshi3.com=103; _tp=OADpdcaf9w1gvwf3KXvMTA==; _pst=leonardo_zhou; __jdc=76161171; ip_cityCode=1158; thor=0BEE90145C8E1871FCCEE59402B4731537EC64664D4D91C48C77903DC5CE5D4BF8A8C73A7397F5F7F17FA6CB2297C178BE50C2768FDCB85CFB9AF3CBB86C2C98B8B4D00350A814C947CC4E07AE9EFD3820C885C7F774E53A81E6B3AD7F8640CE79A7A019DB7C09AC78529F9D3EB449F591695894859D5405F47716313B5F00CDBA68099ABA20C36797EE004827B9596A; 3AB9D23F7A4B3C9B=QTHFY3RGF3DKN4LZ46HMGTX4YRLMWY5G3H2NVEHV53GZKJ3I4EMEOPJKCF2C7MQXRVG5BPEP4TRABBZ4GEEI6PG7YE; __jda=76161171.16405043962681952968723.1640504396.1640529504.1640566240.4; __jdb=76161171.1.16405043962681952968723|4.1640566240; shshshsID=7a510cfa1983a5e59671f7970d5c93dd_1_1640566242033',
	'user-agent': random.choice(UA_list)
}
with open('ip.json', 'r') as file:
	proxies = json.load(file)
	ip_address = random.choice(proxies)
	proxy = {
		"http": 'http://{}:{}'.format(ip_address['ip'], ip_address['port'])
	}

with open('t.html','wb') as file:
	content = requests.get(url,headers,proxies=proxy).content
	file.write(content)
	print(content)
# with open('ip.json', 'r') as file:
# 	proxies = json.load(file)
# 	proxy = {
# 		"http": random.choice(proxies)
# 	}

# print(requests.get(url,headers=headers,proxies=proxy).content.decode('utf-8'))
# temp = {'存储': '256G固态硬盘 + 500G机械硬盘', '处理器或显卡': 'i7-8565U(4核)/MX250独显', '颜色': '16G内存'}
# for i in temp.values():
# 	print(i)