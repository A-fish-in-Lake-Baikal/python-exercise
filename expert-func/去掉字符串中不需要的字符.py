# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/8/9 20:45
'''

s = ' abc\t789\tajdl ldo        '

p = s.strip()
p1 = s.lstrip()
p2 = s.rstrip()
p3 = s.replace('\t','')
print(p)
print(p1)
print(p2)
print(p3)