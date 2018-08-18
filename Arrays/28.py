haystack = "mississippi"

needle = "issip"
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    s1 = 0
    s2 = 0
    c = 0
    while(s1 < len(haystack)):
    	print(s2,c)
    	if needle[s2] == haystack[s1] and c == 0 :
    		if s2 == len(needle)-1:
    			print("Found at {}".format(s1 - s2))
    			return s1 - s2
    		s2 += 1
    		c = -1

    	elif c  == -1 and needle[s2] == haystack[s1]:
    		#print("hgfuy",s2)
    		if s2 == len(needle)-1:
    			print("Found at {}".format(s1 - s2))
    			return s1 - s2
    		s2 += 1
    	elif c  == -1 and needle[s2] != haystack[s1]:
    		c == 0
    		print(s1,s2, "rhirh")
    		s1 = s1 - (s1- s2 + 1)
    		s2 = 0
    	s1 +=1
    return -1

#print(strStr(haystack,needle))


############################# Solution 2 #################################################
def strStr2(haystack, needle):
	l = len(needle)
	for i in range(0,len(haystack) ):

		print(haystack[i:i +l], type(needle))
		if haystack[i:i+l] == needle:
			return i
	return - 1
print(strStr2(haystack,needle))
