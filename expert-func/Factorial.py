# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/29 21:27
'''

def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)


if __name__ == '__main__':
    s = f(4)
    print(s)