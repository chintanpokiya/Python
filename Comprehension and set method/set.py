'''
Name : Parekh Neelkanth
Div : c 
Er no : 22004500210151
Topic : set
Time : 10:15
Day : Tuesday
'''

'''
set - a set is an unordered collection of elements much like a set in a mathematics.
set a = {1,2,3}
set b = {-9,12,13,14,0}
does not accept duplicate values
set is mutuable so we can modify it 
set are unordered so we can not access its element using index
sets are represented using curly brackets {}.
a = {10,20,30,"Neelkanth","Parekh",40}


ADD()
we can add a new element to set using add() method.
syntax:-
    set_name.add(new_element)


ADD MULTIPLE ELEMENTS
we can add multiple to set using update() method
Syntax:- 
    set_name.update(elements)
a.update([101,102,103])

we can delete element using remove() or discard() methods.

copy method is use to copy existing sets elements into another set.


some other methods of set

intersection()
union()
difference()
issubset()
issuperset()
'''

a={10,20,"Neelkanth","Parekh",40,-10}
b={20,30,50,"Parekh","Neelkanth",10}
c={10,20,30,"Hello","World",45}
# print(a[0])
print(a)

a.add(30)
print("After adding a new element in set is :- ",a)

a.update([101,102,103])
print("After updating a element in a set is :- ",a)

#the update method can take tuples lists strings etc.... 
# a.update(104,105,106)
# print("After updating a element in a set is :- ",a)

# a.remove(101)
# a.discard(102)
# print(a)
# print(b)

n={"Hello","World",40,32,56}

new_a=a.copy()
new_a.update(a,b)
print(a)
print(new_a)