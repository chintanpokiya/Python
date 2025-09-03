#method overriding

class Add:
    def result(self,a,b):
        print('Addition:',a+b)

class Multi(Add):
    def result(self,a,b):
        super().result(10,20)
        print('Multiplication:',a*b)

m = Multi()
m.result(10,20)

