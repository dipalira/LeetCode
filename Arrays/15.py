nums =  [-1, 0, 1, 2, -1, -4]
def threeSum( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    curr_2 = 0
    curr_3 = 0
    result = []
    for i in range(0,len(nums)):
    	start,end = i,len(nums -1 )

    	while (start <  end):
	    	curr_2 = nums[end] + nums[start] + nums[i]
	    	if curr_2 == 0:
	    		print(nums[end],nums[start] ,nums[i])
	    		break
	    	elif curr_2 < 0:
	    		start +=1
	    	else:
	    		end -=1
