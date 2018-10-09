# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/9 20:11
'''

def convert(time):
    if time[-1] in ['Y','y']:
        convert_time = int(time[:-1])*12*30*24*60
        print("%s 转换后为 %dminute" %(time,convert_time))
    elif time[-1] in ['M','m']:
        convert_time = int(time[:-1])*24*60*30
        print("%s 转换后为 %dminute" %(time,convert_time))
    elif time[-1] in ['D','d']:
        convert_time = int(time[:-1])*24*60
        print("%s 转换后为 %dminute" %(time,convert_time))
    else:
        print("输入错误，请重新输入！")



if __name__ == '__main__':
    time = input("请输入带有单位的时间：")
    convert(time)