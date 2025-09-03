#nested dictionary

a={1:{'course':'python','fees':10000},
  2:{'course':'javascript','fees':10000}}

#accessing nested dicitonary
print(a[1]['course'])
print(a[2]['fees'])
print()

print("Original :- ")
print(a)
print()

#modifying nested dictionary
a[1]['course']='Machine Learning'
a[2]['fees']=5000
print("After Modification :- ")
print(a)
print()


#deletion
del a[1]['course']
print("After Deletion :- ")
print(a)
print()

#add new item
a[1]['duration']='6 months'
a[2]['Teacher']='Neelkanth Parekh'
print("After Addition :- ")
print(a)
print()

#after dictionary inside dictionary
a[3]={'course':'ReactJS','fees':10000}
print("After Adding a Dict :- ")
print(a)
print()

#sumof fees
sum=0
for id in a:
    sum=sum+a[id]['fees']
print(sum)
print()