class Set():
    def __init__(self,value = []):
        self.data = []
        self.concat(value)

    def intersect(self,other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self,other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self,value):
        for x in value:
            if not x in self.data:
                self.data.append(x)



if __name__=='__main__':
    x = Set([1,3,5,7])
    print(x.union(Set([1,4,7])))
    print(Set([1,4,6]))