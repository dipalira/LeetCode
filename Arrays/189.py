class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        for i in range(0,k):
            r = nums.pop()
            nums.insert(0,r)
            #print(nums)
        
