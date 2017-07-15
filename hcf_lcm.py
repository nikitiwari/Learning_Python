print "Enter two numbers to find hcf and lcm"
x = raw_input("Enter m :")
y = raw_input("Enter n :")
try :
    m= (int)(x)
    n=(int)(y)
    if m == n:
        print "HCF is ", m
    elif m > n :
        a=m
        b=n
    elif m<n :
        a=n
        b=m
    while a%b != 0 :
        r=a%b
        a=b
        b=r
    print "HCF is ",b
    print "LCM is ", (m*n)/b
        
except :
    print "Only Numbers allowed"
