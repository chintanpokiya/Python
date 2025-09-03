'''
Name : Parekh Neelkanth
Div : c 
Er no : 22004500210151
Topic : set methods
Time : 10:36
Day : Tuesday
'''

# set methods

a = {'Neelkanth','Jaimin','Mukesh','Sachin'}
b = {'Devraj','Karan','Krunal','Python','Java'}

print("A:- ",a)
print("B:- ",b)
print()

#intersection() method
    #returns item which exists in both sets
ism = a.intersection(b)
print("Intersection :- ",ism)
print()


#union() method
    #returns all item from original set and all items from specified set
um = a.union(b)
print("Union :- ",um)
print()


#difference() method
    #returns items that exists only in first set, and not in both sets
dm = a.difference(b)
print("Difference :- ",dm)
print()


#issubset() method
    #returns true if all items in the set exists in the specified set
isub = a.issubset(b)
print("Issubset :- ",isub)
print()


#issuperset() method
    #returns true if all items in the specified set exists in the original set
isup = a.issuperset(b)
print("Issuperset :- ",isup)
print()