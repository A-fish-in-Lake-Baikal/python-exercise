# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/8 20:56
'''

import re

s = r'sija,sigli;oai|laido|djliae\tlsaiefl;\t'

r = re.split(r'[,;\t|]+',s)
print(r)