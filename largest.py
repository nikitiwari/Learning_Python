print "The largest among the three numbers."
inp = raw_input("Enter a number: ")
x= (int)(inp)
inp = raw_input("Enter a number: ")
y= (int)(inp)
inp = raw_input("Enter a number: ")
z= (int)(inp)
if x>y and x>z :
    print x," is the largest."
elif y>x and y>z :
    print y, "is the largest."
else :
    print z, "is the largest."