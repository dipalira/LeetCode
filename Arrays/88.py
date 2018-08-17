nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        s1 ,s2= 0,0	
        while((s1 < m+n ) and (s2 <n )):
            if nums1[s1] >=  nums2[s2]:
                nums1 = nums1[:s1] + [nums2[s2]] + nums1[s1:-1]
                s2 += 1
                s1 += 1
                
            elif nums1[s1] == 0 and s2 < n:
                for i in range(s2, len(nums2)):
                    nums1 = nums1[:s1] + [nums2[i]] + nums1[s1:-1]	    	
            else:
                s1 += 1
        print(nums1)    	