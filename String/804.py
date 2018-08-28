words = ["gin", "zen", "gig", "msg"]
def uniqueMorseRepresentations( words):
    """
    :type words: List[str]
    :rtype: int
    """
    count = 0
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ouput = []
    for word in words:
    	val = ''
    	w = list(word)
    	
    	for x in w:
    		val+= code[ord(x)-ord('a')] 
    	if val in ouput:
    		continue
    	else:
    		ouput.append(val)
    return len(ouput)
print(uniqueMorseRepresentations(words))