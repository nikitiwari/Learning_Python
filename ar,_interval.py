print "Armstrong in an interval"
inp=raw_input("Enter the initial:")
x=(int)(inp)
inp=raw_input("Enter the end:")
y=(int)(inp)
i=x
while (i<(y+1)) :
    sm=0
    n=i
    while n!=0 :
        r=n%10
        sm=sm+r*r*r
        n=n/10
    if sm==i :
      print i
    i=i+1