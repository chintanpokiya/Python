'''
Name : Parekh Neelkanth
Div : c 
Er no : 22004500210151
Topic : Dictionary
Time : 11:50
Day : Wednesday
Date : 14/08/2024
'''

'''
when and why ?
array
    store group of elements of same datatype
    array uses less memory
list
    store group of elements of same or different datatype
    lists are mutuable so we can modify it
tuple
    same or diff datatype
    tuples are immutable
    occupy less memory compare to list
set
    unordered group of elements of same or diff datatype
    does not accept duplicate elements
dictionary
    store elemets in the form of key value pair same or different datatype
    dictionary in python is an unordered collection
    dictionaries are mutable so we can modify its items 


Dictionary :-

    a dictionary represents a group of elements in the form of key value pair
    dictionary in python is an unordered collection.
    dictionaries are mutable so we can modify its item , without changing their identity.
    dictionaries are represented using curly brackets{}.
    same as set

    Ex:-
        stu={101:'Neelkanth',102:'Jimmy',103:'Mukesh'}
        fees={'Neelkanth':2000,'Jimmy':3000,'Mukesh':4000}
        print(stu)
        print(fees)

    syntax :- 
        dict_name = {}
        ex:- fees={}


creating a dictionary :- 
    a dictionary is created in the form of key-value pair where keys can't be repeated and must be immutable and values can be of any datatype and can be duplicated.
    keys are case sensitive
    syntax:-
        dict_name = {key1:value1,key2:value2,.....}

fees={
    'rahul':3000
    'soham':5000
    'raj':8000
}

key rules:-
    while writing key we must follow the following rules:
        key should be unique 
        if we mention same key again, the old key will be overwritten
        key should be immutable type ex:- integer,string or tuple
        we can not use list or dictionary as key.

accessing dictionary
    we can access the value of a dictionary by referring to its key name, inside square brackets
    stu = {101:'rahul',102:'raj',103:'soham'}
    fees = {'rahul':2000,'raj':4000,'soham':8000},

modifying
    we can modify the existing value of key by assigning a new value.
    stu = {101:'rahul',102:'raj',103:'soham'}
    stu[102]='Python'

Insert/add new item
    we can add an item to dictionary just by mentioning a new key-value pair into an existing dictionary.
    if we mention a key which is already exists in the dicitonary then the value gets updated/modified rather than adding a new item
    the new item may be added at any place in the dictionary as dictionary is an unordered collection.
    stu = {101:'rahul',102:'raj',103:'soham'}
    stu[104]='NeelkanthParekh'


deletion
    we can delete an item of dictionary or entire dictionary using del statement
    stu = {101:'rahul',102:'raj',103:'soham'}
    

testing key 
    we can check whether a key is already exists in the dicitonary or not, for this purpose we use membership operator.
    stu = {101:'rahul',102:'raj',103:'soham'}
    
    101 in stu #if exists returns true
    104 not in stu # if not exists returns true

clear() method 
    this method is used to remove all the elements from the dicitonary.

copy() method
    this method is used to copy all the elements from the existing dicitonary into a new dictionary.
    dict.copy()

fromkeys() method
    this method is used to create a new dicitonary with the specified keys and values 
    syntax:-
        dict.fromkeys(keys,value)
    Ex:-
        key=(101,102,103)
        value="Neelkanth"
        new_stu=dict.fromkeys(key,value)

get() method
    this method returns the value of the specified key.
    if kwy is not found then it will return none or default value.
    Syntax:
        dict_name.get(key,defaultvalue)
    Ex:-
        stu.get(104)
        stu.get(104,'Neelkanth')

items() method
    this method returns an object that contain key-value pairs of dicitonary
    the pairs are stored as tuples in the object.
    Syntax:-
        dict_name.items()
    Ex:-
        stu.items()

keys() method
    this method returns a sequence of keys from the dicitonary.
    Syntax:-
        dict.name.keys()
    Ex:-
        stu.keys()

 values() method
    this returns a sequence of values from the dictionary
    Syntax:-    
        dict_name.value()

update method()
    this method is used to update the dicitonary with the specified key value pair
    Syntax:-
        dict_name.update(iterable)
    Ex:-
        stu.update({105:'Neelkanth'})

pop() method
    this method is used to remove the item with specified key.
    it returns the removed item's value.
    if key is not found then the a default value is returned.
    if key is not found and default value is not given then shows keyError.

popitem() method
    this method is used to remove the item which was last inserted into the dictionary.
    it returns the removed item in the form of tuple, Pairs are returned in LIFO order.
    Synatx:-
        dict_name.popitem()
    Ex:-
        stu.popitem()

setdefault() method
    this method returns the value of the specified key.
    if key is not found then it inserts key with the specified value.
    Syntax:-
        dict_name.setdefault(key,value)
    Ex:-
        stu.setdefault(101,'Neelkanth')
'''

#create dictionary
stu={101:'Neelkanth',102:'Jimmy',103:'Mukesh'}
# fees={'Neelkanth':2000,'Jimmy':3000,'Mukesh':4000}
# print(stu)
# print(fees)
# del stu[102]
# print(stu)

# print(101 in stu)
# print(104 not in stu)


# key = (101,102,103)
# value = 'Neelkanth'
# new_stu = dict.fromkeys(key,value)
# print(new_stu)

# print(stu.items())
# print(stu.keys())
# print(stu.pop(101))
# print(stu.pop(101,'CVG'))

# a={}
# n=int(input("Number of elements :- "))

# for i in range(n):
#     k = input("Enter Key :- ")
#     v = input("Enter Value :- ")
#     stu.update({k:v})

# print(stu)


# print(stu[101])

# #display keys
# for k in stu:
#     print(k)

# #display values
# for k in stu:
#     print(stu[k])


# roll = [10,11,12]
# name = ['Neel','Muk','Jai']

# #make a dictionary
# z = zip(roll,name)
# d = dict(z)

# print(d)
# for k in d:
#     print(k,'=',d[k])
