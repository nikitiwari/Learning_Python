import math
print "Convert decimal number to binary and octal"
x=(int)(raw_input("Enter a decimal(base 10) number:"))
ch=(int)(raw_input("Enter choice:1.BInary 2.Octal  :"))
sm=0
i=0
if(ch==1) :
    while(x!=0) :
        r=x%2
        sm=sm+r*(math.pow(10,i))
        i=i+1
        x=x/2
    print (int)(sm)
elif ch==2 :
    while(x!=0) :
        r=x%8
        sm=sm+r*(math.pow(10,i))
        i=i+1
        x=x/8
    print (int)(sm)
else :
    print "Wrong choie"