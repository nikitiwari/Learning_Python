print "Swapping the values of two variables using a third variable :-"
inp = raw_input("Enter the value of a: ")
a = (int)(inp)
inp = raw_input("Enter the value of b: ")
b = (int)(inp)
c = b
b = a
a = c
print a ,"and", b
print "Again Swapping resultant values of two variables WITHOUT using a third variable :-"
a=a+b
b=a-b
a=a-b
print a ,"and", b