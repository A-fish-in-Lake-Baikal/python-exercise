#保留两位小数
a = "%.03f"%1.3335
print(a,type(a))

b = round(float(a),1)
print(b)

c = round(float(a),2)
print(c)

A = zip(("a","b","c","d","e"),(1,2,3,4,5))
AO = dict(A)
print(AO)

