print " to check a number whether prime or not "
inp =  raw_input("Enter a number: ")
x = (int)(inp)
i=2
while (i!=x):
    if x%i == 0 :
        break
    i=i+1
if x == 2 :
    print "Prime Number."
else :
    if i == x :
	    print "Prime number."
    else :
        print "Not a prime number."
