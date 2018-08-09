#An integer x is said to be Noble in arr[] if the number of integers greater than x are equal to x.
#x = [-1, -9, -2, -78, 0]
#Test Cases
#x = [7, 3, 16, 10,3]
x.sort()
for i in range(0,len(x)):
	#print(len(x) - i-1)
	if x[i] == len(x) - i-1:
		print(x[i])
print(x)