s = "A man, a plan, a canal: Panama"
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    start = 0
    end = len(s) - 1
    s = list(s)
    while (start < end):
    	s[start], s[end] = s[end] ,s[start]
    	start+= 1
    	end -=1
    return ''.join(s)
print(reverseString(s))