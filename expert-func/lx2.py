bonus1 = 100000*0.1
bonus2 = bonus1+100000*0.75
bonus3 = bonus2+200000*0.5
bonus4 = bonus3+200000*0.3
bonus5 = bonus4+400000*0.15
while True:
    i = int(input("请输入利润："))
    if i<= 100000:
        bonus = i*0.1
    elif i<=200000:
        bonus = bonus1+(i-100000)*0.075
    elif i<=400000:
        bonus = bonus2+(i-200000)*0.5
    elif i<600000:
        bonus = bonus3+(i-400000)*0.3
    elif i<1000000:
        bonus = bonus4+(i-600000)*0.15
    else:
        bonus = bonus5+(i-1000000)*0.1
    print("%s" %bonus)