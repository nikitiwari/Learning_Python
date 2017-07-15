print "Factorial of a number using recursion"
n = (int)(raw_input("Enter a number :"))
def fact_n( x) :
    if x == 1 :
        return 1
    else :
        return (x*fact_n(x-1))
print fact_n(n)