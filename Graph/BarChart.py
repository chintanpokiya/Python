#To display employees of 4 department
import matplotlib.pyplot as plt

#Take the percentage of employees in 4 department
slices = [25,25,20,15,15]

#Take the percentage of employees of 4 department
depts = ['IT','Sales','Production','HR','Finance']

#Take the percentage of employees of 4 departments
cols=['cyan','magenta','red','gold','pink']

#create a pie chart
plt.pie(slices,labels=depts,colors=cols,startangle=90,explode=(0,0,0.2,0,0),shadow=True, autopct='%.2f%%')

#set titles and legends
plt.title('LOK JAGRUTI KENDRA UNIVERSITY')
plt.legend(loc='lower center',bbox_to_anchor=(0.5,-0.15),ncol=2)

#Show the Pie Graph
plt.show()
