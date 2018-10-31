# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/15 21:10
'''

def DayDayUp(df):
    dayup = 1.0

    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup

dayfactor = 0.01
while DayDayUp(dayfactor) < 37.78:
    dayfactor += 0.001

print("努力指数:{:.3f}".format(dayfactor))