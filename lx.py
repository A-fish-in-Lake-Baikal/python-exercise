import urllib.request
import re
import os
from lxml import etree

class Spider:

    def __init__(self):
        self.siteURL='http://www.mm131.com/'
        self.curCount=0
        self.maxCount=0

    def getPage(self,url):
        hearders = {
                    'Connection': r'keep-alive',
                    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': r'gzip, deflate',
                    'Accept-Language': r'zh-CN,zh;q=0.8',
                    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
        requset=urllib.request.Request(url)
        response=urllib.request.urlopen(requset)
        return response.read().decode('gbk')

    def getContents(self,url):
        page=self.getPage(url)
        tree = etree.HTML(page)
        regChildUrl="/html/body/div[@class='content']/div[@class='content-pic']/a/@href"
        nextChildUrl = tree.xpath(regChildUrl)[0]
        picUrl=tree.xpath("/html/body/div[@class='content']/div[@class='content-pic']/a/img/@src")[0]
        picName = tree.xpath("/html/body/div[@class='content']/div[@class='content-pic']/a/img/@alt")[0]
        contents=[picName,picUrl,nextChildUrl]
        return contents

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print(u"正在偷偷保存她的个人信息为", fileName)
        f.write(content.encode('utf-8'))

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        self.curCount=self.curCount+1
        print(u"正在悄悄保存一张美女图片为", fileName)
        f.close()

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print("偷偷新建了名字叫做", path, "的文件夹")
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            #print("名为"+path+"的文件夹已经创建成功")
            return True

    def saveUrlPic(self,url):
        if self.curCount>self.maxCount:
            return
        else:
            contents=self.getContents(url)
            # 保存图片
            paths = contents[1].split('/')[::-1]
            path="./"+paths[1]
            bMkdir = self.mkdir(path)
            if not bMkdir:
                return
            else:
                fileName = path + '/' + paths[0]
                self.saveImg(contents[1], fileName)
                nextChildPageUrl = contents[2]
                urlSplit=nextChildPageUrl.split('/')
                if len(urlSplit)<2:
                    nextChildPageUrl = self.siteURL + nextChildPageUrl
                self.saveUrlPic(nextChildPageUrl)

    def getTypeFirstUrl(self,type):
        typeurl=self.siteURL+type
        page=self.getPage(typeurl)
        tree = etree.HTML(page)
        reg = "/html/body/div[@class='main']/dl[@class='list-left public-box']/dd[1]/a/@href"
        return tree.xpath(reg)[0]


    def savePic(self,size):
        self.maxCount=size;
        picType=[
            {"name":"性感美女","type":"xinggan"},
            {"name":"清纯美眉","type":"qingchun"},
            {"name": "美女校花", "type": "xiaohua"},
            {"name": "性感车模", "type": "chemo"},
            {"name": "旗袍美女", "type": "qipao"},
            {"name": "明星写真", "type": "mingxing"}
        ]
        print("现在美女类型如下：\n")
        i=1
        for type in picType:
            print(str(i),":",picType[i-1].get('name', 0))
            i=i+1
        inttype=int(input("请选择想要爬取的类型，输入对应的序号：\n"))
        typename=picType[inttype-1].get('type', 0)
        firstUrl=self.getTypeFirstUrl(typename)
        self.siteURL=self.siteURL+typename+"/"
        self.saveUrlPic(firstUrl)
#
spider = Spider()
spider.maxCount=int(input("请输入想抓取的图片数量:\n"))
spider.savePic(spider.maxCount)
