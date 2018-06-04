class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i in range(0,len(nums)):
            if nums[i] in seen:
                val = seen[nums[i]]
                if abs(i - val) <=k:
                    #print(i,val)
                    return(True)
            seen[nums[i]] = i
        return False