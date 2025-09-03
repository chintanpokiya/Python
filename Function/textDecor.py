#function decorator
#example 1 
'''def decor(fun):
    def inner():
        print("inner function : before enhancing function")
        fun()
        print("inner function : after enhancing function")
    return inner

def num():
    print("We will use this function")
    print("and will enhance this in decorator")

result_fun = decor(num)
result_fun()'''


#example 2

def decor(fun):
    def inner():
        print("inner function : before enhancing function")
        fun()
        print("inner function : after enhancing function")
    return inner
@decor
def num():
    print("We will use this function")
    print("and will enhance this in decorator")
num()