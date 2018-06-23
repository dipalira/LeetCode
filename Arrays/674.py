class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_, current_=  0,0
        if len(nums) == 0: return 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current_ += 1
            else:
                current_ = 0
            max_ = max(current_, max_)
        return max_ +1