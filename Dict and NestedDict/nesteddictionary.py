'''
nested dictionary :-
    a dicitonary within another dicitonary is called as nested dictionary or nesting of a dictionary.
    {'dict1':{'Key_A':'value_!}},

empty nested dictionary
Syntax:-
    nested_dict = {'dict1':{},
                    'dict2':{}}

created nested dictionary
a={'course':'python','fees':15000,1:{'course':'javascript','fees':10000}}
'''

# a={'course':'python','fees':15000,1:{'course':'javascript','fees':10000}}
# print(a)
# print(a['course'])
# print(a['fees'])

# print(a[1]['course'])
# print(a[1]['fees'])

# #modify 

# a['course']="ML"
# a[1]['fees']=40000
# print(a)


#nested dictionary

a={'course':'python','fees':15000,1:{'course':'javascript','fees':10000}}

#accessing nested dicitonary
print(a['course'])
print(a['fees'])
print(a[1]['course'])
print(a[1]['fees'])
print()

print("Original :- ")
print(a)
print()

#modifying nested dictionary
a['course']='Machine Learning'
a[1]['fees']=200000
print("After Modification :- ")
print(a)
print()


#deletion
del a[1]['course']
print("After Deletion :- ")
print(a)
print()

#add new item
a['duration']='6 months'
a[1]['Teacher']='Neelkanth Parekh'
print("After Addition :- ")
print(a)
print()

#after dictionary inside dictionary
a[2]={'course':'ReactJS','fees':30000}
print("After Adding a Dict :- ")
print(a)
print()