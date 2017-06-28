print "Addition of two numbers"
inp = raw_input("Enter an Integer:")
input = raw_input("Enter another Integer: ")
try :
    x= (int)(inp)
    y = (int)(input)
    print (x+y)
except:
    print "Enter an Integer only"