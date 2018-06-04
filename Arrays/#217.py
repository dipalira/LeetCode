class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) <= 1:
            return False
        seen = {}
        c  = False
        for i in nums:
            if i in seen:
                return True
                break
            seen[i] = 1        
        return c