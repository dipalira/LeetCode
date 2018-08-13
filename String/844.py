S = "ab#c"
T = "ad#c"
def backspaceCompare( S, T):
	"""
	:type S: str
	:type T: str
	:rtype: bool
	"""
	return compare(S) == compare(T) 
def compare(S):
	out = ''
	skip = 0
	for i in S[::-1]:
		if i == '#':
			skip += 1
		elif  i != '#' and skip == 0:
			out += i 
			skip = 0
		elif i != '#' and skip > 0:
			skip -= 1
	print(out)
	return out

print(backspaceCompare(S,T))



class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return compare(S) == compare(T)
    def compare(S):
        out = ''
        skip = 0
        for i in S[::-1]:
            if i == '#':
                skip += 1
            elif  i != '#' and skip == 0:
                out += i 
                skip = 0
            elif i != '#' and skip > 0:
                skip -= 1
        print(out)
        return out
