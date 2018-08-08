import requests
from collections import Iterator,Iterable

class WeatherIterator(object):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getweather(self,city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city='+city
        response = requests.get(url)
        data = response.json()['data']['forecast'][0]
        return '%s:%s ,%s' %(city,data['low'],data['high'])
        # print(response.text)
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getweather(city)
if __name__ == '__main__':
    cities = ['北京','上海','广州','深圳','浙江','兰州']
    W = WeatherIterator(cities)
    W.getweather()