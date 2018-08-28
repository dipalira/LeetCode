s = "abcdefg" 
k = 2

def reverseStr( s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    run = len(s)//(2*k)
    start = 0
    print(run)
    s = list(s)
    for i in range(0,run):
    	s[start:start + k] = reversed(s[start:start + k])
    	start += 2*k
    if len(s[start:]) <k:
    	s[start:] = s[start:][::-1]
    else:
    	s[start:start + k] = s[start:start + k][::-1]
    return "".join(s)
print(reverseStr(s,k))
