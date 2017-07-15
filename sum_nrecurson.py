print "Sum of n natural numbers using recursion"
n = (int)(raw_input("Enter a number :"))
def sum_n( x) :
    if x == 1 :
        return 1
    else :
        return (x+sum_n(x-1))
print sum_n(n)