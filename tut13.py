from traceback import print_tb


var1 = 3
var2 = 7

var3 = int(input())
if var3>var2:
    print("greater")
elif var3==var2: 
    print("equal")   
else:
    print("lesser")    

print("type ur age to check driving eligibility")

age = int(input())

if age>18:
    print("u can drive")
elif age == 18:
    print(" u can drive")
else:
    print( " not e;igible to drive")
