# -*- coding: utf-8 -*-
# @Author  : 马维畅
# @Time    : 2020/1/3 13:34
# @File    : dic_test.py

ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", \
      "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合", \
      "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范", \
      "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合", \
      "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
d = {}
for word in ls:
    d[word] = d.get(word, 0) + 1

print(d)

for k in d:
    print("{}:{}".format(k, d[k]))
