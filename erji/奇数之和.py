# -*- coding: utf-8 -*-
# @Author  : 马维畅
# @Time    : 2020/1/22 10:49
# @File    : 奇数之和.py

import random

N = eval(input("请输入一个整数："))
s = 0
for i in range(N,N+100):
    if i%2==1:
        s += i

print(s)