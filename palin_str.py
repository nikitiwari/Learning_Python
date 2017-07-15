print "Enter a String to check whether its palindrome or not"
st= (raw_input("Enter st :")).lower()
s = st[::-1]
if st == s :
    print "It is a palindrome string"
else :
    print "It is not a palindrome string"
