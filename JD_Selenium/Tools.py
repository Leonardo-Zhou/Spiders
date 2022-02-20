# -*- coding: utf-8 -*-
"""
@File    : Tools.py
@Time    : 2022/2/11 21:10
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

from BlockWord import BLOCKWORDS

class Tools:
    def delete_not_ascii(self, string):
        string = ''.join([i for i in string if '0' <= i <= '9' or 'a' <= i <= 'z' or 'A' <= i <= 'Z' or i == '.'])
        return string
    
    def delete_block_words(self, string):
        def get_length(i):
            return len(i)
        
        # 用于将BLOCKWORDS按照字符串长短倒序排序，这样可以先删除掉长的字符串
        BLOCKWORDS.sort(key=get_length, reverse=True)
        
        for i in BLOCKWORDS:
            string = string.replace(i, '')
        return string

if __name__ == '__main__':
    tool = Tools()
    # s = '秒杀价￥7999'
    s = '联想笔记本电脑 拯救者R9000P 16英寸高性能电竞游戏本(标压 8核 R7-5800H 16G 512G RTX3060 2.5k屏 165Hz)'
    # print(tool.delete_not_ascii(s))
    s1 = tool.delete_block_words(s)
    print(s1)