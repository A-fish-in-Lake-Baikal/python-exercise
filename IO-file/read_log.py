# coding=utf-8
'''
author:马维畅
time：2019/1/21 10:45
'''

import os, sys, re


def lastline():
    global pos

    while True:
        pos = pos - 1
        try:
            f.seek(pos, 2)  # 从文件末尾开始读
            if f.read(1) == '\n':
                break
        except:  # 到达文件第一行，直接读取，退出
            f.seek(0, 0)
            print(f.readline().strip())

            return

    print(f.readline().strip())


if __name__ == "__main__":

    f = open('elasticsearch-2019-02-21.log', 'rb')  # ‘r’的话会有两个\n\n
    pos = 0
    for line in range(10):  # 需要倒数多少行就循环多少次
        lastline()
    f.close()
