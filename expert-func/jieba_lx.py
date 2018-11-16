# coding=utf-8
'''
author:马维畅
time：2018/11/12 13:33
'''

import jieba


def getwords(path):
    counts = {}
    ptn = {"将军","二人","不可"}
    text = open(path,"r",encoding="utf-8").read()
    words = jieba.lcut(text)
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
    for word in ptn:
        del counts[word]
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word, count))



if __name__ == '__main__':
    path = input("请输入需要分词的文本路径：")
    getwords(path)