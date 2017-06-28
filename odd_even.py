print "Check the number whether even or odd."
inp = raw_input("Enter an integer:")
try :
    x=(int)(inp)
    if x%2 ==0 :
	    print "Even"
    else :
        print "Odd"
except :
    print"Only Integer required."