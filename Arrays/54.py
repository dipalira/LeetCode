def spiralOrder( matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator 
    """
    m = len(matrix[0])
    n = len(matrix)
    output_ = []
    while len(output_ ) <= m*n:
	    try:
	    	output_+= matrix.pop(0)  #1
	    	for row in range(0,len( matrix)):   #2
	    		output_.append(matrix[row].pop(-1))
	    	print(matrix)
	    	output_ += matrix.pop(-1)[::-1]    #3
	    	for row in reversed(range(0,len( matrix))):  #4
	    		output_.append(matrix[row].pop(0))
	    except:
	    	break

    print(output_)
spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])