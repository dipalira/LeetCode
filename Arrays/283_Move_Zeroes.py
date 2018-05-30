class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = 0
        l = len(nums)
        index =[]
        t =0 
        while c <l:
            #print(nums[i])
            if nums[t] == 0:
                nums.pop(t)
                nums.append(0)
            else: 
                t +=1
            #print(nums)
            c += 1