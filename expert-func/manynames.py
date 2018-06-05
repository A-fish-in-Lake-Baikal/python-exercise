x = 11
def f():
    print(x)

def g():
    x = 22
    print(x)

class c:
    '''wojdka;kdjie;ajkd;faiea;j;dkgjaie;fkajd;kaejoifja;dkjfeiflja;dkf'''
    x = 33
    def m(self):
        x = 44
        self.x =55

if __name__=='__main__':
    print(x)
    f()
    g()
    print(x)

    obj = c()
    print(obj.x)

    obj.m()
    print(obj.x)
    print(c.x)

    print(obj.__doc__)
    # print(c.m.x)
    # print(g.x)