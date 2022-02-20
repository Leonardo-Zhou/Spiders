# -*- coding: utf-8 -*-
"""
@File    : 测试raise一场.py
@Time    : 2022/2/19 21:57
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

class NotOkException(Exception):
    pass


try:
    raise NotOkException
except NotOkException:
    print('捕捉成功')