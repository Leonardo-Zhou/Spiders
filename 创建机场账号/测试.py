# -*- coding: utf-8 -*-
"""
@File    : 测试.py
@Time    : 2021/11/21 11:31
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import random
import numpy as np
import time
import requests
# a1=np.array([[11,12,13,14,15],[21,22,23,24,25]])
# print(a1)
# print(a1[:2,:3])


def time_test():
    start = time.time()
    sum = 0
    n = 10000000
    for i in range(n):
        sum += 255
    end = time.time()
    print('255相加使用的时间为{}'.format(end - start))

    start = time.time()
    sum = 0
    for i in range(n):
        sum += 1
    end = time.time()
    print('1相加使用的时间为{}'.format(end - start))


def test_list():
    d = {
        'level': 'INFO',
        'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.jssrvpn.xyz/auth/register","frameId":"F3EF9E4D55CB28D164969EFDF5EA25FC","hasUserGesture":false,"initiator":{"stack":{"callFrames":[{"columnNumber":9,"functionName":"loadScript","lineNumber":148,"scriptId":"16","url":"https://static.geetest.com/static/tools/gt.js"},{"columnNumber":8,"functionName":"tryRequest","lineNumber":193,"scriptId":"16","url":"https://static.geetest.com/static/tools/gt.js"},{"columnNumber":4,"functionName":"load","lineNumber":211,"scriptId":"16","url":"https://static.geetest.com/static/tools/gt.js"},{"columnNumber":4,"functionName":"jsonp","lineNumber":241,"scriptId":"16","url":"https://static.geetest.com/static/tools/gt.js"},{"columnNumber":4,"functionName":"window.initGeetest","lineNumber":310,"scriptId":"16","url":"https://static.geetest.com/static/tools/gt.js"},{"columnNumber":4,"functionName":"","lineNumber":417,"scriptId":"20","url":"https://www.jssrvpn.xyz/auth/register"}]},"type":"script"},"loaderId":"30B60A4173598B9809C21EEF4D34CDBA","request":{"headers":{"Referer":"https://www.jssrvpn.xyz/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/96.0.4664.45 Safari/537.36","sec-ch-ua":"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://api.geetest.com/gettype.php?gt=0150cbbcf473ca04c6ac745a4ff7aac1&callback=geetest_1637587266728"},"requestId":"13000.67","timestamp":1159.980555,"type":"Script","wallTime":1637587258.73989}},"webview":"F3EF9E4D55CB28D164969EFDF5EA25FC"}',
        'timestamp': 1637587258743}


def test_web():
    url = 'https://api.geetest.com/ajax.php?gt=0150cbbcf473ca04c6ac745a4ff7aac1&challenge=cb0020cce80c7a780588d190d3b47cff7x&lang=zh-cn&%24_BBF=0&client_type=web&w=GalHBMXrR6PONSdlOq9hXifCKmMETXNvw66sfEp6IaDeHh8604DEzJnwGUtYNOPuEarwplxD7Y5jwQ5VrilFb5tDH7wobys83zlXkMpKuMyRooxyxgx0hABSl7uCRLKDolr4e9hLAkSJmfPVl9AuoAga7DCYdrg3opTiNqUADH2)d05OPurnRfgtINDY(sP1P15J)PgCiTt2B3lA5yCLi14nB5HgvJCZeAapzs23ETIBtVCqsusdwkpKFH2EJqCtkGCpTI9aqnFArGl9xOKFkDAzIWPrK30iQ1OzZDtiBlf86Zz8CtVMjihCTvQ66iJoYGRY9GmVKowrjBYR5Q5dmj2aTWciWfPxfmhFwNSTmXA3AjHtgmKQkPTlZCs7((CecpBde(sajzy2cd4aORqxuUO6NZWZNQTtgt8C7JZfmxUEU)CvwyVRkf83fO5(aR0HG8a3rOo2rO)5)2JRJr33uN8y7xv5rc6lNr9(n9TzjPQZ3sdEEm0QdcQT9BHRTvuhQ1ilUcdDNnrlhuIECZmPJ0x685qb743w3q9zKD8nYirIPV04AH4APZ6MM8mjjhVJShTcxueB4KLEL8aapCrjaM739XSYWyPueafy9cUE7RG6fbpiboxrfY)gGTki7ZRRKC9LNnxAqvb2AxZxUDw(4bSr0sUQQk2kzp79yXhuQ3mkZOi9xTYzbWSZiUZHv7HcdqzvuNWEYTV6wNpr4l2Fe62W3WEnDdfsObsKlAd5(hxc7kT)VBDc85aZ3wArNlswHlzQcE2ZB5FkqoOWXNxCJRii08lQ78fG2ZAFn97ZFhYdVJaACuqDknyeowsI195NLMF6cqU9Dno9v9rD93hCUQNtaJEObR(EduKlMFZ4X6iWIorN0PJ5IokZSvpeMGEsb7dnz8ywLchwLGsDE8bOzR1s5vCr)ErJHEf3RdgFRZpFb0v(ph)CtokrZQRPFYwzYarUrZNP2PzMCCYA1RXawD25js))d8KTiu)nu6yh3FSigOpYOQw9Jo3TF5pC((SVpyf(r(TATj7J1qwR24rTdw..b0272a60c7bf98f67c422a5556398d8471058dbedc237ac1d413e2ae68b96ca5577ac34117d2a68ca1c0d87d821044912cd1efd015012b057123b8ff210b7ed32683bc71f32e84f462a231511db61a0a2d4d05759c6b0f601725ef19eb0b985cd63acb9f003d1723aca50487f341fad92c0085a0819ad8110fdd35a67ef721cd&callback=geetest_1637589485522'
    headers = {
	'Accept-Encoding': 'gzip, deflate, br' ,
	'Accept-Language': 'en,zh-TW;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6' ,
	'Connection': 'keep-alive' ,
	'Host': 'api.geetest.com' ,
	'Referer': 'https://www.jssrvpn.xyz/' ,
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' ,
	'sec-ch-ua-mobile': '?0' ,
	'sec-ch-ua-platform': '"Windows"' ,
	'Sec-Fetch-Dest': 'script' ,
	'Sec-Fetch-Mode': 'no-cors' ,
	'Sec-Fetch-Site': 'cross-site' ,
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36' ,
}
    
    response = requests.get(url, headers=headers)
    print(response.content)

if __name__ == '__main__':
    # time_test()
    test_web()