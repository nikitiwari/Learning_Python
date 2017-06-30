print "Check armstrong number"
inp=raw_input("Enter the number to be checked:")
x = (int)(inp)
n=x
sm=0
while n!=0 :
    r=n%10
    sm=sm+r*r*r
    n=n/10
if x==sm :
    print "It is an Armstrong Number"
else :
    print "Not an Armstrong number"