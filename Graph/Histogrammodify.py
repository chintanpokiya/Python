import matplotlib.pyplot as plt
import pandas as pd

#Example data : department and employee count
data = {
    'Department' : ['HR','IT','Finance','Marketing','Sales'],
    'Employee Count' : [10,20,30,40,50]
    }

#create a dataframe
df = pd.DataFrame(data)

#create a bar chart
plt.figure(figsize=(10,6))
plt.bar(df['Department'],df['Employee Count'],color='purple')

#Add titles and labels

plt.title('Number of Employess by Department')
plt.xlabel('Department')
plt.ylabel('Employee Count')

#Display the count on the top of the bars

for i, count in enumerate(df['Employee Count']):
    plt.text(i,count + 0.5,str(count),ha='center')

plt.show()
