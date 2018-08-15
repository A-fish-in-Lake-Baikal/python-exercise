# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/9 20:25
'''

s = 'abc'
d = {
    'Distcull':500.0,
    'Smallcull':0.04,
    'farclip':477,
    'lodDist':100.0,
    'trilineat':40
}

p1 = s.ljust(20,'*')
p2 = format(s,'>20')

w = max(map(len,d.keys()))
for k in d:
    print(k.rjust(w),':',d[k])

print(p1)
print(p2)