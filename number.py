print "Identify the number"
inp = raw_input("Enter an integer:")
try :
    x = (int)(inp)
    if x>0 :
        print "The given number is positive."
    elif x<0 :
        print "The given number is negative."
    elif x==0 :
        print "The given number is zero."
except :
    print "Only Integer required"	
