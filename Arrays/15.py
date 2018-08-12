nums = [-2,0,0,2,2]
#threeSum([-25,-10,-7,-3,2,4,8,10])

def threeSum( nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	nums.sort()
	curr_2 = 0
	curr_3 = 0
	result = []
	if len(nums) <3 :
            return []
    elif all( v == 0 for v in nums):
        return [[0,0,0]]

	for i in range(0,len(nums)):
		start,end = i + 1,len(nums )-1 
		if nums[i] == nums[i-1] :
			#print('f')
			continue
		else:
			while (start <  end):
				curr_2 = nums[end] + nums[start] + nums[i]
				print(nums[end],nums[start] ,nums[i], curr_2)
				if curr_2 == 0:
					result.append([nums[end],nums[start] ,nums[i]])
					while start < end and nums[start] == nums[start+1]:
						start += 1
					while start < end and nums[end] == nums[end-1]:
						end -=1
					end -=1
					start += 1
				elif curr_2 < 0:
					start +=1
				elif curr_2 > 0:
					end -=1

	print (result)
threeSum(nums)
