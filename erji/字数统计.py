# -*- coding: utf-8 -*-
# @Author  : 马维畅
# @Time    : 2020/1/22 13:56
# @File    : 字数统计.py


with open("./成神.txt","r",encoding="gb18030") as f:
    l = f.read()
    d = {}
    # ps = ["","\n","《","》","：","？","，","。","！","【","】","、","（","）","“","”"]
    for i in l:
        if '\u4e00' <= i <= '\u9fff':
            d[i] = d.get(i,0)+1
    l = sorted(d.items(),key=lambda x:x[1],reverse=True)
    for x in l:
        # print(x)
        x = list(x)
        with open("./test.txt","a",encoding="utf-8") as f:
            f.write("{}:{}\n".format(x[0],x[1]))
        print("{:<}:{:>}".format(x[0],x[1]))