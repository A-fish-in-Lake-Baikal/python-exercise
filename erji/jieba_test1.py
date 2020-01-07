# -*- coding: utf-8 -*-
# @Author  : 马维畅
# @Time    : 2020/1/7 17:01
# @File    : jieba_test1.py

import jieba

s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
# 标点符号字数
n = s.count(",")+s.count("?")
# 中文字数
m = len(s)-n


print("标点符号个数:{},汉字个数:{}".format(n,m))
