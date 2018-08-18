
nums = [1,2,3,4,5]
k = -1
def findPairs( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n = len(nums)
    l,r = 0,0
    count = 0
    nums.sort()
    while (r < n):
    	print(nums[r],nums[l])
    	if nums[r] - nums[l] == k and r != l or nums[r] - nums[l] == -1*k:
    		count += 1
    		l += 1
    		r+= 1
    	elif nums[r] - nums[l] > k:
    		l+=1
    	else:
    		r+=1
    return count
print(findPairs(nums,k))