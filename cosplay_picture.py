# -*- coding:utf-8 -*-
import time
from urllib import request
from bs4 import BeautifulSoup
import re

urls = ['http://www.cosplay0.com/cosplayfuli/20180226/534_{}.html'.format(str(i)) for i in range(2,14)]

for url in urls:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode('utf-8')
    soup = BeautifulSoup(page_info, 'html.parser')
    # Beautiful Soup和正则表达式结合，提取出所有图片的链接（img标签中，class=**，以.jpg结尾的链接）
    links = soup.find_all('img',alt=r'绝对领域女仆远坂凛美女私房黑丝诱惑Cosplay足控福利', src=re.compile(r'.jpg$'))
    with open(r'F:\pic\url.txt','a') as file:
        for link in links:
            file.write(url+'\n'+link.attrs['src']+'\n')
    '''links_a = soup.find_all('a', href=re.compile(r'.html$'))
    with open(r'F:\pic\links.txt', 'w') as file:
        for link_a in links_a:
            print(link_a.attrs['href'])
            file.write(link_a.attrs['href'] + '\n')'''
# 设置保存的路径，否则会保存到程序当前路径
    local_path = r'F:\Pic'
    for link in links:
        print(url+'\n'+link.attrs['src'])
        # 保存链接并命名，time防止命名冲突
        request.urlretrieve(link.attrs['src'], local_path + r'\%s.jpg' % time.time())