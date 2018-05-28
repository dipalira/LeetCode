# Time:  O(n)
# Space: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count+= 1
            else:
                if count > ans:
                    ans = count       
                count = 0
        if count >ans :
            return count
        else:
            return ans
