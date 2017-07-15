print "Enter a number to print its factors"
x = raw_input("Enter x :")
try :
    m= (int)(x)
    print "Factors of ",m,":-"
    i=1
    while i<=m :
        if m%i ==0 :
            print i
        i=i+1
except :
    print "Only Numbers allowed"
