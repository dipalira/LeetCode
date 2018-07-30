def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ### All negative and postive array
    if all(num < 0 for num in nums):
    	return max(nums)
    elif all(num > 0 for num in nums):
    	return sum(nums)

    else:
    	curr_sum,max_sum = nums[0],nums[0]
    	for arr in nums[1:]:
    		if curr_sum + arr > 0:
    			
    			curr_sum = curr_sum + arr
    		else:

    			curr_sum = 0
    			print(max_sum)
    		max_sum = max(curr_sum + arr,max_sum)
    	return max_sum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))