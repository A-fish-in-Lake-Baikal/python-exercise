# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/11/20 21:44
'''
import jieba
import wordcloud

f = open("Hamlet.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700,background_color="white",font_path="msyh.ttc")
w.generate(txt)
w.to_file("grwordcloud.png")
