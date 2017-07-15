import calendar
import datetime
print "Enter month and year to display the calender"
mon = raw_input("Month:")
yr = raw_input("Year :")
try :
    m = (int)(mon)
    y = (int)(yr)
    print(calendar.month(y, m))
    print  "Current Date and Time are :-"
    print datetime.datetime.now()

except :
    print "Only Numbers allowed"