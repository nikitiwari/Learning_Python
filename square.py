inp = raw_input("Enter an integer:")
try:
    x = (int)(inp)
    print "Square root is", x*x
    print "Cube root is " ,x*x*x
except:
    print "Integer required"
	