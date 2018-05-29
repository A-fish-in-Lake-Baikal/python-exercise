

class person(object):
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def first_name(self):
        return self.name.split()[0]
    def giveraise(self,percent):
        self.pay = int(self.pay*(1+percent))

if __name__=='__main__':
    b = person('Bob smitch')
    s = person('sue jones','It',5000)
    print(b.name,b.job,b.pay)
    print(s.name,s.job,s.pay)
    print(b.first_name(),s.first_name())
    s.giveraise(0.1)
    print(s.pay)
