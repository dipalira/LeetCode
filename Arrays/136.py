class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = {}
        for i in nums:
            if i in out:
                out.pop(i)
            else:
                out[i] = 1
        return list(out.keys())[0]