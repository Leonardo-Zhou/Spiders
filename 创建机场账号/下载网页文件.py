# -*- coding: utf-8 -*-
"""
@File    : 下载网页文件.py
@Time    : 2021/11/23 15:11
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
s=requests.session()
url = 'https://www.jssrvpn.xyz/auth/login'
user_url = 'https://www.jssrvpn.xyz/user'
check_in_url = 'https://www.jssrvpn.xyz/user/checkin'
data = {
'email': 'dBQNdaKjfSHEyrt@gmail.com',
'passwd': '12345678',
'code': None
}

r1 = s.post(url, data)

response = s.get(user_url,headers=headers)
with open('initial.html','wb') as file:
    file.write(response.content)
    
r2 = s.post(check_in_url)

response = s.get(user_url,headers=headers)
with open('after.html','wb') as file:
    file.write(response.content)




