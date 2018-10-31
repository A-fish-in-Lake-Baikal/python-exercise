# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/23 21:21
'''

from random import random
from time import perf_counter

darts = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,darts+1):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <=1.0:
        hits = hits+1
pi = 4*(hits/darts)
print("圆周率是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter()-start))