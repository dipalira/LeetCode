numRows = 6
output = [[1]*i for i in range(1, numRows+1 )]
print(output)
for row_ in range(2,len(output)):
	row = output[row_]
	for i in range(1,len(row)-1):
		try:
			output[row_][i] = output[row_-1][i] + output[row_-1][i-1]

		except IndexError:
			continue
print(output)