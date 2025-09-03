#To display employees of 4 department
import matplotlib.pyplot as plt

#Take the Years(sales) for Profit in a year
Years = ['2012','2013','2014','2015','2016','2017']

#Take the profit of the sales in year 
Profits = [9,10,10.5,8.8,10.9,9.75]

#create a line chart
plt.plot(Years,Profits,'blue')

#set titles and legends
plt.title('LOK JAGRUTI KENDRA UNIVERSITY')
plt.xlabel('Years')
plt.ylabel('Profits')
plt.legend(loc='lower center')

#Show the Pie Graph
plt.show()
