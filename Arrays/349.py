nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
def intersection( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    start1 = 0
    start2 = 0
    nums1.sort()
    nums2.sort()
    out = []
    while (start1 < len(nums1) and start2 < len(nums2)):
    	if nums1[start1] < nums2[start2]:
    		start1 +=1
    	elif (nums1[start1]  == nums2[start2]) and (nums1[start1]  != nums1[start1-1]) :
    		out.append(nums1[start1])
    		start1 +=1
    		start2 +=1
    	elif nums1[start1] > nums2[start2]:
    		start2 +=1
    return out

print(intersection(nums1,nums2))