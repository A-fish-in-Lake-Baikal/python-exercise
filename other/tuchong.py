import requests
import time
import random
import json
import os

class FigureWorm(object):
    def __init__(self):
        pass

    def RunCrawler(self,url):
        response = requests.get(url)
        data = json.loads(response.text)
        ImageBox = []
        for UserAlbum in data['postList']:
            AuthorID = str(UserAlbum['author_id'])
            for s_image in UserAlbum['images']:
                ImageID = str(s_image['img_id'])
                ImageUrl = "http://photo.tuchong.com/"+AuthorID+"/f/"+ImageID+".jpg"
                ImageName = AuthorID+"-"+ImageID+".jpg"
                ImageInfo = {
                    "ImageURL":ImageUrl,
                    "ImageName":ImageName
                }
                ImageBox.append(ImageInfo)
        print(ImageBox)
        print("本页共有{}张图片".format(len(ImageBox)))
        # print(json.dumps(data, ensure_ascii=False, indent=4))

        for img in ImageBox:
            if os.path.isfile("./pic/"+img["ImageName"]):
                print(img["ImageName"]+"---已存在！")
                continue
            else:
                time.sleep(random.randint(1,3))
            self.DownImage(img["ImageURL"],img["ImageName"])

    def DownImage(self,ImageURL,FileName):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        if not os.path.isdir("./pic/"):
            os.mkdir("./pic/")
        response = requests.get(ImageURL, headers=header, stream=True)
        chunk_size = 1024*1024
        with open("./pic/"+FileName,"wb+") as f:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
            print("{}--保存成功".format(FileName))

if __name__=="__main__":
    urls = ["https://tuchong.com/rest/tags/%E7%A7%81%E6%88%BF/posts?page={}&count=20&order=weekly".format(str(i)) for i in range(1,10)]
    c = 1
    for url in urls:
        print("第{}页：".format(c))
        c+=1
        P = FigureWorm()
        P.RunCrawler(url)
