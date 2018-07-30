#Note that because the order of covering the points is already defined, the problem just reduces to figuring out the way to calculate the distance between 2 points (A, B) and (C, D).
def coverPoints( A, B):



	output = 0
	for i in range(0, len(A)):
		#print(i,j)
		try:
			dist = (A[i] - A[i+1])**2 + (B[i] - B[i+1])**2
			print(dist)
			output += dist**(1/2)

		except:
			continue


	print(int(output))

coverPoints([ -7, -13 ], [ 1, -5 ])