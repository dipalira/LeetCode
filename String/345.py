s = "leetcode"
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    start = 0
    end = len(s) - 1
    s = list(s)
    vowels = set(list("aeiou"))
    while (start < end):
        if (s[start] in "aeiou") and (s[end] in "aeiou" ):
            s[start], s[end] = s[end] ,s[start]
            start +=1
            end-=1
        elif s[start] not in "aeiou":
            start +=1
        elif s[end] not in "aeiou":
            end -= 1
        
    return ''.join(s)
print(reverseString(s))