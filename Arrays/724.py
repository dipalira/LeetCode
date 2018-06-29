def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currentsum_ = 0
    sum_ = sum(nums)
    for i in range(0,len(nums)):

        rightsum_ = sum_ - currentsum_ - nums[i]
        if currentsum_ == rightsum_:
            return i 
        currentsum_ += nums[i]
    return -1
nums = [1, 2, 3]
print(pivotIndex(nums))
