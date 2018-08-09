row = [1,1]
k = 4
for row_ in range(2,k+1):
	output = [1]*(row_+1)
	print('klrjg')	
	for i in range(1,len(output)-1):
		try:
			print(i-1, i)
			output[i]  = row[i-1] + row[i]
		except:
			continue
	row = output
	print(row)