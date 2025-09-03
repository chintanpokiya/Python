'''
W.A.P
'''
try:
    num1=float(input("Enter Num 1:- "))
    num2=float(input("Enter Num 2:- "))
    res = num1/num2
    print(res)
    
except ValueError as ve:
    print(ve)

except TypeError as te:
    print(te)

except Exception as e:
    print(e)
