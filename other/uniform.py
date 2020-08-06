import random
random.seed()
n=eval(input("请输入一个整数："))
sum=0
for i in range(n):
    f1 = random.uniform(1,100)
    sum+=f1
    print(f1)
print("the average is:{},sum is {}".format(sum/n,sum))
