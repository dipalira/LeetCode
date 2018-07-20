<<<<<<< HEAD
nums = [1,3,5,6]
target = 5
"""def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
    print(lower,upper)
binary_search(nums,target)"""
for x in range(0,len(nums)):
	if nums[x] > target:
		print(nums[x])
		print(x-1)
		break
	else:
		print(x)
=======
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index_ = 0
        
        for num in nums:
            if num < target:
                index_ += 1
        return index_
>>>>>>> 16f982d039b7c1aeda7eaeba42023e88cbad991c
