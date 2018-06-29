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
