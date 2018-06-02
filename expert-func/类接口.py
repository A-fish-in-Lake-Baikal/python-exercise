class Super(object):
    def method(self):
        print('in Super.method')
    def delegate(self):
        print('tiis is delegate')
        self.action()

class Inheritors(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    def method(self):
        print('strting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')
        # assert False, 'action must be defined'

if __name__=='__main__':
    for klass in (Inheritors,Replacer,Extender):
        print('\n'+klass.__name__+'...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()