#Example 5

class Mobile:
    #constructor
    def __init__(self,m):
        self.model = m
        print("I am calling automatically..!!")

    def show_model(self,p):
        price = p
        print("Model :- ",self.model,"and Price :- ",price)

#creating object of class
Vivo = Mobile('Vivo Y56 5G')

#accessing method from outside class
Vivo.show_model(1000)
