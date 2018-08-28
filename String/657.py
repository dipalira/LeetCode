moves = "UD"
def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    dic = {"D": [0,-1],"U":[0,1],"L": [-1,0],"R":[1,0]}
    x,y = 0,0
    for move in moves:
    	step = dic[move]
    	x+= step[0]
    	y+= step[1]
    if x == 0 and y == 0:
    	return True
    else: 
    	return False
print(judgeCircle(moves))