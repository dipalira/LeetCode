class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = max(nums)
        
        ind =  nums.index(max_)
        for i in nums :
            if 2*i > max_ and i != max_:
                print(i)
                return -1 
        return ind
        