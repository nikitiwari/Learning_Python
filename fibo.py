print "Fibonacci sequence"
inp=raw_input("Enter the total length of sequence required :")
x=(int)(inp)
a=0
b=1
print a
print b
i=3
while i<(x+1) :
    c=a+b
    print c
    a=b
    b=c
    i=i+1