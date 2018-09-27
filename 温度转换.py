# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/9/19 20:49
'''

Tempstr = input('请输入带有符号的温度值：')
if Tempstr[-1] in ['F','f']:
    c = (eval(Tempstr[0:-1])-32)/1.8
    print('转换后的温度是{:.2f}℃'.format(c))
elif Tempstr[-1] in ['C','c']:
    f = 1.8*eval(Tempstr[0:-1])+32
    print('转换后的温度是{:.2f}F'.format(f))
else:
    print('输入的格式错误')