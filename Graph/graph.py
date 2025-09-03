#import visualization module

import matplotlib.pyplot as plt
import pandas as pd

#create data dictionary
empdata = {'empid':[1001,1002,1003,1004,1005,1006,1007] ,
                  'ename':['Neelkanth Parekh','Ganesh Rao','Anil Kumar','Gaurav Gupta','Hema Chauhan','Laxmi Prasant','Anant Garg'],
                  'sal' : [10000 ,10000,23000.5,18000.33,16500.5,12000.75,9999.99],
                  'doj' : ['02-02-2002','10/10/2000','3/20/2002','3/3/2002','9/10/2000','10/8/2000','	9/9/1999']}
print(empdata)

#dictionary convert into dataframe

df = pd.DataFrame(empdata)
print(df)

#extract employee id and salary into x and y axis

x = df['empid']
y = df['sal']

#create bar chart(it is a function of pyplot lib)

plt.bar(x,y,label='Employee Data',color=['red','green','pink','purple','yellow','cyan','blue'])

plt.title("LOK JAGRUTI KENDRA UNIVERSITY")

plt.xlabel("Employee IDs")

plt.ylabel("Employee Salaries")

#plt.xticks(

plt.legend()

plt.show()

