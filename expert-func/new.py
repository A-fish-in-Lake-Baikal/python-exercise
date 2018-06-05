class Index():
    data = [5,6,7,8,9]
    def __getitem__(self,index):
        print('getitem:',index)
        return self.data[index]

class Squares():
    def __init__(self,start,stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

if __name__=='__main__':
    # x = Index()
    # print(x[2:4])
    # for i in range(5):
    #     #     print(x[i],end=' ')
    for i in Squares(1,5):
        print(i,end=' ')