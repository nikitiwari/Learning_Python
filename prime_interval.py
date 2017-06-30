import math
print "Prime numbers in a gievn interval"
inp = raw_input("Enter the beginning:")
x=(int)(inp)
inpt=raw_input("Enter the end:")
y=(int)(inpt)
i=x
while i<(y+1) :
    a = i
    j=2
    f=0
    while j<(int)(math.sqrt(a))+1 :
        if(a%j==0) :
            f=1
            break
        j=j+1
    if(f==0) :
        print a
    i=i+1
