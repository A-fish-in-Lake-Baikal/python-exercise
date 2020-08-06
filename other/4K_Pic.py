import requests
from lxml import etree
import os
import sys

if __name__ == "__main__":

    message_list = ['fengjing','meinv','youxi','dongman','yingshi','mingxing','qiche','dongwu','renwu','meishi','zongjiao','beijing']
    print(
        '''
        软件简介：本程序主要下载4k图片，您可根据您的需求进行下载！！！
        软件作者：---喧啸
                 《下载选择目录》
        ******************************
        ** 风景 美女 游戏 动漫 影视 明星 **
        ** 汽车 动物 人物 美食 宗教 背景 **
        ******************************
        '''
    )
    choice = str(input("请输入您的下载选择(由于本人水平有限，输入时请输入对应的拼音):"))
    if choice in message_list:
        print("下载准备中，请稍后！！！")
    else:
        print("输入出错，请按照要求输入！！！")
        sys.exit()

    page_url = "http://pic.netbian.com/4k" + choice + "/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    page = requests.get(url=page_url, headers=headers)
    page_txt = page.text

    # 数据解析 SRC属性值 ALT的值
    tree1 = etree.HTML(page_txt)
    max_page = tree1.xpath('//div[@class = "page"]/a[7]/text()')[0]
    print("温馨提示!!! "  + "您爬取的网页最大页码为",max_page)

    page = int(input("请输入最大页码:"))
    for i in range(1,page+2):
        url = page_url + "index_" + str(i) + ".html"

        response = requests.get(url = url,headers = headers)
        response.encoding = "gbk"
        page_text = response.text

        #数据解析 SRC属性值 ALT的值
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class = "slist"]//li')
        if not os.path.exists('./picLibs'):
            os.mkdir('./picLibs')
        for li in li_list:
            # ./表示的是当前目录下面进行操作
            img_list = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
            title_list = li.xpath('./a/img/@alt')[0] + ".jpg"
            #print(title_list,img_list)

            img_data = requests.get(url = img_list,headers = headers).content
            img_path = './picLibs/' + title_list
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(title_list,"保存成功！！！")