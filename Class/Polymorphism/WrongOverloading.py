#Wrong Method Type
#this method overloading concept is not available in python
#so it will show error

class Myclass:
    def sum(self,a):
        print("1st Sum Method",a)

    def sum(self):
        print("2nd Sum Method")

obj = Myclass()
obj.sum()
obj.sum(10)
