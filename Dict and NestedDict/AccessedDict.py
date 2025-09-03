#nested dictionary

a={1:{'course':'python','fees':15000},
  2:{'course':'javascript','fees':10000}}

#accessing Id
print("ID :- ")
for id in a:
    print(id)
print()

#accessing each id keys
for id in a:
    for k in a[id]:
        print(k)
print()

#accessing each id keys -- value
for id in a:
    for k in a[id]:
        print(id,'=',k,'=',a[id][k])