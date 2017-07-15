print "Enter a string containig punctuations to print the string without it"
st = raw_input("String :")
word=""
for i in xrange(len(st)-1) :
 #if st[i] in "abcdefghijklmnopqrstuvwxyz " or st[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
    if (st[i]>="a" and st[i]<="z") or (st[i]>="A" and st[i]<="Z") or st[i] == " " :
        word = word +st[i]
print word