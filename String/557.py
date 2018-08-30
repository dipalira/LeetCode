s =  "Let's take LeetCode contest"
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    start = 0
    end = 0
    for i in range(0,len(s)):
    	if s[i] == ' ' or i == len(s)-1:
    		s[start:i+1] = reversed(s[start:i+1])
    		start = i+1

    return "".join(s)
print(reverseWords(s))