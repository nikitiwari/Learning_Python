print "Sorting of words"
print "Enter a choice : 1. sort words in a sentence 2.sort alphabets in words"
ch = (int)(raw_input())
st = raw_input("String :")
if ch == 1 :
    w = st.split()
    w.sort()
    print " ".join(w)
elif ch== 2 :
    w=[]
    for i in xrange(len(st)) :
        w.append(st[i])
	w.sort()
    print "".join(w)
else :
    print "Invalid Input"
