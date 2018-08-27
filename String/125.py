s= "A man, a plan, a canal: Panama"
a = "ab@a"
def isPalindrome( s):
	"""
	:type s: str
	:rtype: bool
	"""
	if len(s) <0 : return True
	r,l = len(s)-1,0
	while l<r:
		if s[r] == ' ' or s[r] in '()[].,:;+@-*/&|<>=~$':
			r-=1
			continue
		elif s[l] == ' ' or  s[l] in '()[].,:;+-*/&|<>=~$':
			l+=1
			continue
		if s[r].lower() == s[l].lower():
			r-= 1
			l+= 1			 
		else:
			print(s[r],s[l],r,l)
			return False
	return True

print(isPalindrome(a))
print(len(s))