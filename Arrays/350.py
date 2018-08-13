nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
def convert2dict(l):
	dnum = dict()
	for i in l:
		if i in dnum:
			dnum[i] +=1
		else:
			dnum[i]  = 1
	return dnum
def intersect(nums1, nums2):
	
	output = []
	dnum1 = convert2dict(nums1)
	dnum2 = convert2dict(nums2)
	print(dnum2,dnum1)
	for key in dnum1:
		if key in dnum2:
			
			output += [key]*min(dnum2[key],dnum1[key])
	return output
print(intersect(nums1,nums2))
def convert2dict(l):
	dnum = dict()
	for i in l:
		if i in dnum:
			dnum[i] +=1
		else:
			dnum[i]  = 1
	return dnum
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        dnum1 = convert2dict(nums1)
        dnum2 = convert2dict(nums2)
        print(dnum2,dnum1)
        for key in dnum1:
            if key in dnum2:

                output += [key]*min(dnum2[key],dnum1[key])
        return output
