#Display Bar Graphs with ids salaries for two depts(Sales and Purchases)

import matplotlib.pyplot as plt

#Takes Employee ids and salaries

#Ids and salaries of sales department
x = [1001,1003,1005,1007,1009,1011]
y = [1000.00,12000.00,15000.00,10000.00,9000.33,5000.50]


#Ids and salaries of production department
x1 = [1002,1004,1006,1008,1010,1012]
y1 = [11000.00,21000.00,51000.00,11000.00,19000.33,15000.50]

#create multiple bar graph

plt.bar(x,y,label="Sales Department",color='red')
plt.bar(x1,y1,label="Production Department",color='yellow')
#plt.tick
#set the labels and legend and title

plt.xlabel('Employee Ids')
plt.ylabel('Employee Salaries')
plt.legend()
plt.title('LOK JAGRUTI KENDRA UNIVERSITY')

#display the multiple bar graph
plt.show()

