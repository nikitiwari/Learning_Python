print "Check whether the hyear is leap year or not:-"
inp = raw_input("Enter a year.")
try:
    x=(int)(inp)
    if (x%4==0 and x%100!=0)or x%400==0 :
        print "Leap Year."
    else :
        print "Not a leap year."
except:
    print "Enter an integer only."