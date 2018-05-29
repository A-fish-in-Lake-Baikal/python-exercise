

class person(object):
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def first_name(self):
        return self.name.split()[0]
    def giveraise(self,percent):
        self.pay = int(self.pay*(1+percent))
    def __str__(self):
        return '[person:%s,%s]' %(self.name,self.pay)

class manager(person):
        def giveraise(self,percent,bonus=.10):
            person.giveraise(self,percent+bonus)
if __name__=='__main__':
    b = person('Bob smitch')
    s = person('sue jones','It',5000)
    c = manager('tomsen wils','banzhuan',6000)
    print(b)
    print(s)
    print(c)
    c.giveraise(.10)
    print(c.pay)
    print(b.first_name(),s.first_name())
    s.giveraise(0.1)
    print(s.pay)
    print("-----all three-----")
    for object in (b,s,c):
        object.giveraise(.10)
        print(object)