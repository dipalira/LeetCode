s= "A man, a plan, a canal: Panama"
a = "abdba"
def validPalindrome( s):
	"""
	:type s: str
	:rtype: bool
	"""
	if len(s) <0 : return True
	r,l = len(s)-1,0
	c = 0
	while l<r:
		if s[r].lower() == s[l].lower():
			r-= 1
			l+= 1			 
		else:
			l+=1
			if s[]
	return True

print(validPalindrome(a))
print(len(s))