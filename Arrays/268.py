class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ran_ = range(len(nums)+1)
        t_ =  sum(ran_) - sum(nums)

        return t_