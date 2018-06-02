class NextClass(object):
    def printer(self,text):
        self.message = text
        print(self.message)



if __name__=='__main__':
    x = NextClass()
    x.printer("wo jiao ma weichang !")
    print(x.message)