nums = []
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur = 0
    i = 1
    while(i < len(nums)):
    	if nums[cur] == nums[i]:
    		nums.pop(i)

    	#print(nums)
    	else:
    		cur += 1
    		i += 1
    return nums 
print(removeDuplicates(nums))