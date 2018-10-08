# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/3 14:05
'''

import requests

def GetHtmlText(url,kv):
    try:
        response = requests.get(url,params=kv)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        print(response.request.url)
        print(response.text)
    except:
        return "产生异常"



if __name__ == '__main__':
    URL = "http://www.baidu.com"
    kv = {'wd':'python'}
    GetHtmlText(URL,kv)
