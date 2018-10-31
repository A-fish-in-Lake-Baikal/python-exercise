# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/15 20:40
'''
dayup = 1.0
dayfactor = 0.019

for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)




print("向上:{:.2f}".format(dayup))