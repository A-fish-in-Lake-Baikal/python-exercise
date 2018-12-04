# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/11/7 21:02
'''

def getText():
    txt = open("./Hamlet.txt","r").read()
    txt = txt.lower()
    pt = '!#$%&()*+,-.\'/:;<=>?@[\\]^_{|}~‘’'
    for ch in pt:
        txt = txt.replace(ch," ")
    return txt

if __name__ == '__main__':
    hanletTxt = getText()
    words = hanletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    # print(items)
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))