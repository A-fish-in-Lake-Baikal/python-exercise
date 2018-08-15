# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/15 20:46
'''

import struct

f = open('July - Hyacinth.mp3','rb')
info = f.read(3)

e = struct.unpack('h',info[1:3])
print(e)
print(info)