#Example 4

class Mobile:
    def __init__(self):
        self.model = 'Vivo Y56 5G'
        print("I am calling automatically..!!")

    def show_model(self):
        price = 1000
        print("Model :- ",self.model,"and Price :- ",price)

#creating object of class
Vivo = Mobile()

#accessing variable from outside class
print(Vivo.model)

#assign variable a new value
Vivo.model='Vivo Y56 6G'

print(Vivo.model)

#accessing method from outside class
Vivo.show_model()
