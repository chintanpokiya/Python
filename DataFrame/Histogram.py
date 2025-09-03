#Display histogram of employee ages
import matplotlib.pyplot as plt

#Takes employee ages
emp_ages = (11,10,1,3,10,34,56,44,78,20,22,56,54)

#Takes ranges values (Bins)

bins = [1,10,20,30,40,50,60,70,80,90,100,110,120,130]

#create histogram graph

plt.hist(emp_ages,bins,histtype='bar',rwidth=0.8,color='green')


#Set the labels and legend and title

plt.xlabel('Employee Ages')
plt.ylabel('No of Employees')
plt.title('LOK JAGRUTI KENDRA UNIVERSITY')
plt.legend()

#Display the histogram graph
plt.show()           
