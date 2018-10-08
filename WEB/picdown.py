# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/8 21:20
'''

import requests
import time
import os

def getpic(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.content
    except:
        print("连接异常")



if __name__ == '__main__':
    url = "http://img0.dili360.com/ga/M02/49/B7/wKgBzFqo8ySAT4nUAAry7yQ0MW4188.tub.jpg@!rw17"

    root = "e://pic//"
    path = root+"%d.jpg" %time.time()
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        pic = getpic(url)
        with open(path,"wb") as f:
            f.write(pic)
        print("文件保存完成")
    else:
        print("文件已存在")