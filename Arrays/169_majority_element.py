class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = {}
        for i in nums:
            if i in out:
                out[i] += 1
            else:
                out[i] = 1
        v=list(out.values())
        k=list(out.keys())
        return k[v.index(max(v))]

        