class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic ={}

        freq = 0
        item = 0
        if len(nums) == 1:
            return 1
        for i,n in enumerate(nums):
            if n in dic:
                dic[n].append(i)

            else:
                dic[n] = [i]
            if freq < len(dic[n]):
                freq = len(dic[n])
                item = n
            elif freq == len(dic[n]):
                if dic[n][-1] - dic[n][0] +1 < dic[item][-1] - dic[item][0] +1:
                    freq = len(dic[n])
                    item = n
        return dic[item][-1] - dic[item][0] +1