#method overriding

class Add:
    def result(self,a,b):
        print('Addition:',a+b)

class Multi(Add):
    def result(self,a,b):
        print('Multiplication:',a*b)

a = Multi()
a.result(10,20)

m = Add()
m.result(10,20)
