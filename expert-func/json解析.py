# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/9 20:55
'''

import requests
import json


def getweather(url):
    response = requests.get(url)
    jsontexts = json.loads(response.text)
    print(jsontexts)



if __name__ == '__main__':
    citys = ['北京','上海','广州','深圳','沈阳']
    for city in citys:
        url = 'http://wthrcdn.etouch.cn/weather_mini?city='+city
        getweather(url)