#operator overloading

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x = x

a = A(100.34)
b = B(200)
print(a+b)
