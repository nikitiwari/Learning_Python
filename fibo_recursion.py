print "Fibonacci Series upto n terms using recursion"
n = (int)(raw_input("Enter Number of terms required :"))
def fibo_n(x):
    if x <= 1:
        return x
    else:
        return(fibo_n(x-1) + fibo_n(x-2))
	   
	   
print("Fibonacci sequence:")
for i in range(n):
    print(fibo_n(i))