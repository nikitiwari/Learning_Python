print "numbers divisible by a given number"
inp=raw_input("Enter the number by which divisibility is to be checked:")
n=(int)(inp)
x=(int)(raw_input("Enter the range:"))
y=(int)(raw_input("Enter the limit:"))
i=x
while(i<(y+1)) :
    if(i%n==0) :
        print i
    i=i+1
	