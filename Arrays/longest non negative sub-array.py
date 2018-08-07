# Python program to find
# length of the longest
# subarray with
# non-negative numbers.
 
# Function that returns
# the longest subarray
# of non-negative integers 
def longestSubarry(arr,n):
 
    start = 0
    end = 0
    max_length = 1
    curr_length = 0
    for i in arr:
    	if i >= 0 :
    		curr_length = curr_length  + 1 
    		#print(curr_length)
    	else:
    		#print(i)
    		curr_length = 0
    	max_length =  max(curr_length, max_length)
    return max_length
 
 
# Driver code
 
arr= [1, 0, 4, 0, 1, -1, -1, 0, 0, 1, 0]
n = len(arr)
print(longestSubarry(arr, n))
