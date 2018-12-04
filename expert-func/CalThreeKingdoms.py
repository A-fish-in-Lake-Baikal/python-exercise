# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/11/8 20:45
'''

import jieba

txt = open("./ThreeKingdoms.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","军士","左右","军马","引兵","次日","大喜","天下","于是","东吴","今日","不敢","魏兵","陛下","人马","不知"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "周瑜" or word == "都督":
        rword = "周瑜"

    else:
        rword = word

    counts[rword] = counts.get(rword,0) + 1   #rword存在返回相应的值，不存在则返回0
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))