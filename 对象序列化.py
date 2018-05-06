import os
import pickle
path = os.path.abspath('.')
d = [1,2,3,4,5]
b = pickle.dumps(d)
print(path+r'\dump.txt')
with open(path+r'\dump.txt','a') as file:
    file.write(str(b))


f = open('dump.txt','rb')
d = pickle.load(f)
print (d)
f.close()
print(d)