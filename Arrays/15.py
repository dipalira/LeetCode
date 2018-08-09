nums =  [1,2,-2,-1]
def threeSum( nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	nums.sort()
	curr_2 = 0
	curr_3 = 0
	result = []
	if len(nums) <3 or (sum(nums) == 3 and len(nums) == 3):
	    return []

	for i in range(0,len(nums)):
	    start,end = i,len(nums )-1 
	    if nums[i] == nums[i-1] :
	        
	        continue
	    else:
	        while (start <  end):
	            curr_2 = nums[end] + nums[start] + nums[i]
	            print(nums[end],nums[start] ,nums[i], curr_2)
	            if curr_2 == 0:
	            	print("fh")
	            	result.append([nums[end],nums[start] ,nums[i]])
	            	print
	            	end -=1
	            elif curr_2 < 0:
	                start +=1
	            elif curr_2 > 0:
	                end -=1
	print (result)
threeSum(nums)
#threeSum([-25,-10,-7,-3,2,4,8,10])
