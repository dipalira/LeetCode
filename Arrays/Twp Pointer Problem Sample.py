"""
Given a sorted array A, having N integers. You need to find any pair(i,j) having sum as given number X.

"""

A = [1,3,4,6,8,11]
X = 10 
# we keep two pointers, one at the starting tip of the array and another at the tail.
i,j =0, len(A)-1
sum_ = 0
while (i < j):
	sum_ = A[j] + A[i]
	print(A[i],A[j], A[i] + A[j])
	if sum_ == X:
		print("The result is ",A[i],A[j])
		break
	elif sum_  > X:
		j-=1
	else:
		i+=1
