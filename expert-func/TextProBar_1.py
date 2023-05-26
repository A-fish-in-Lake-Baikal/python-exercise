# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/10/18 21:07
'''

import time
scale = 11
starttime = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '~' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - starttime
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)

# bfb = 100
# for i in range(bfb+1):
#     a = i * '*'
#     b = (bfb-i) * '~'
#     c = i%(bfb-1)
#     print("\r{:3.0f}%[{}->{}]".format(c,a,b),end="")
#     time.sleep(1)