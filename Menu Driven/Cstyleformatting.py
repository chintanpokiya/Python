"""Definition : To create a string creation
Author : Neelkanth Parekh
Date of creation : 6/8/2024
Time of creation : Tuesday"""

print("%d" % 432)
print("%d %d" % (432,345))
print("%f" % 432.123)
print("%f %f" % (432.123,10.3))
print("%f" %432.123467)
print("%f"%432.1234567890)
print("%s"%"neelkanthparekh")
print("%s %s"%("Hello","World"))
print("%d %s"%(432,"Neelkanth"))
print("%(nm)s %(ag)d"%{'ag':432,'nm':"Neelkanth Parekh"})


print("% d"%432)
print("%    d"%432)
print("%+d"%432)

print("%8d"%432)
print("%08d"%432)
print("%.3f"%432.123)
print("%.2f"%432.123)