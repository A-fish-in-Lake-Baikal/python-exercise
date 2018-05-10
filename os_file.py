'''import os
# 获取当前目录的绝对路径
print (os.path.abspath('.'))
print (os.path.split('os_file.py'))
# 获取当前路径下的所有py文件
print ([x for x in os.listdir('.') if os.path.isfile(x) and
os.path.splitext(x)[1]=='.py'])

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import this

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%9d  %2s  %s%s' % (fsize, mtime, f, flag))
print(2**100)