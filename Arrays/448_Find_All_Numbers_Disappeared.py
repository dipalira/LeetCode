nums = [4,3,2,7,8,2,3,1]

output = list(range(1,len(nums)+1))
print(output)
for i in nums:
	if i in output:
		output.remove(i)
print(output)