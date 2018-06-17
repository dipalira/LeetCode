class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #O(nlogn)
        k = sorted(nums)
        return max(k[-1]*k[-2]*k[-3], k[0]*k[1]*k[-1])
        
        
        
        
        