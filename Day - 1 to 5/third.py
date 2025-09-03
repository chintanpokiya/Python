#conversion type - one type to another
#IMPLICIT CONVERSION

a = 5
b = 2
value = a/b
print(value)
print(type(value))

x = 10
y = 5.5
total = x + y
print(total)
print(type(total))

j = "Hello"
k = "Neelkanth Parekh"
p = j + k
print(p)
print(type(p))

# q = 20
# u ='10'
# r = q + u
# print(r)

# m = 20
# n = 'Neelkanth'
# t = m + n
# print(t)

#EXPLICIT CONVERSION

# a = 10.5
# b = int(a)
# c = str(a)
# print(type(a))
# print(type(c))

a = 5
b = 2
value = a/b
print(type(value))
int_value = int(value)
print(int_value)
print(type(int_value))

q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r)

#complex
n3 = 10
vn3 = complex(n3)
print(vn3)
print(type(vn3))

#String to Tuple
n5 = "Neelkanth Parekh"
vn5 = tuple(n5)
print(vn5)
print(type(vn5))

#tuple to list
n5 = ("Neelkanth","Mukesh","Jaimin","Sachin")
vn5 = list(n5)
print(vn5)
print(type(vn5))