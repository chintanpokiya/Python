import pandas as pd

df = pd.read_csv("D:\employeedata.csv")
print(df)
print(dir(df))
#Query 10 : Display column name

print(df.columns)

#Query 11 : Display Id

print("print ID :- ")
print(df.empid)

#Query 12 : Display employee id and name

print("employee id and name :- ")
print(df[['empid','ename']])

#Query 13 : Find out min and max salary

print("Min Sal :- ")
print(min(df['sal']))

print("Max Sal :- ")
print(max(df['sal']))


#Query 14 : Display a statistical information min max mean std quartile value
print("Display Statistical data :- ")
print(df.describe())
print(df['empid'].describe())

#Query 15 : Query on data - Display records of those employee whose salary > 10000
print("Query on data - display records of those employee whose salary > 10000")
print(df[df.sal > 10000])

#Query 16 : Display records of those employee whose salary is max

print("Query on data - display records of those employee whose salary is max ")
print(df[df.sal == max(df.sal)])


#Query 17 : Query on data - display empid and employee name whose salary > 10000

print("Query on data - display empid and ename whose salary > 10000 ")
print(df[['empid','ename']][df.sal > 10000])

#Query 18 : Display data of dataframe object 

print(df)

#Query 19 : Concept of indexing 

df1 = df.set_index('empid')
print("Before index set :- ")
print(df)
print("After index set :- ")
print(df1)
#original change
df1=df.set_index('empid',inplace=True)
print(df)
print(df1)

#Query 20 : location

print(df.loc[1001])


#Query 21 : reset index df

df.reset_index(inplace=True)
print(df)

#Query 22 : sort particular value

print("Original Data :- ")
print(df)

df1 = pd.read_csv("D:\employeedata.csv",parse_dates=['doj'])
print(df1)
df1 = df1.sort_values('doj')
print(df1)