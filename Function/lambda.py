'''r=lambda x,y : x + y

def add(x,y):
    return x+y

r=add(2,5)'''

# add=lambda x=10:(lambda y:x+y)
# a=add()
# print(a)
# print(a(20))


# iife - immediately invoked function expressions

'''sum=lambda x:x+1
sum(5)

(lambda x:x+1)(5)

add=lambda x,y:x+y
add(5,2)

(lambda x,y:x+y)(5,2)'''

#iife
'''
(lambda x:print(x+1))(5)
(lambda x,y : print(x+y))(5,2)'''

