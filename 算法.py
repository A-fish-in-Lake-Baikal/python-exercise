# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/9/6 20:14
'''
import time

def printN(i,N):
    while i<=N:
        print(i)
        i += 1



if __name__ == '__main__':
    time1 = time.time()
    printN(1,1000000 )
    time2 = time.time()
    time = time2-time1
    print(time)