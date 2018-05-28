
#matrix = [[1,2,7,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
m = len(matrix[0])
n = len(matrix)
output = False
for i in matrix[:n-1]:
	print(i)



"""for i in range(0,n-1):
	print(set(matrix[i][:m-1]))
	print(set(matrix[i+1][1:]))
	if set(matrix[i][:m-1]) == set(matrix[i+1][1:]):
		output = True
	else:
		output = False
		break
"""


print(output)