import math
print "Implementing calculator"
print "Select operation : 1.Addition 2.Subtraction 3.Multiplication 4.Divide to get quotient"
print "5.Divide to get remainder 6.power :--"
ch = (int)(raw_input())
a = (int)(raw_input("Enter a number:-"))
b = (int)(raw_input("Enter another number:-"))
if ch == 1:
    print a+b
elif ch == 2:
    print a-b
elif ch == 3 :
    print a*b
elif ch == 4 :
    print a/b
elif ch == 5:
    print a%b
elif ch == 6 :
    print math.pow(a,b)
else :
    print "Invalid Input"
    
