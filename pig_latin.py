print "Enter a string to convert to pig latin form"
st = raw_input("string:")
word=""
for i in xrange(len(st)-1) :
    if st[i] in "aeiou" or st[i] in "AEIOU" :
	    break
if i == (len(st)) :
    print st
else :
    print st[i:]+st[0:i]+"ay"