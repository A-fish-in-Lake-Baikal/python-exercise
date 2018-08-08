# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/8 21:01
'''

import os,stat

path = os.listdir('.')
for p in path:
    s = p.endswith('.py')
    print(s)

# print(path)