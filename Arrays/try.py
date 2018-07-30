arr = [3, 1, 3]
 #4, 3, 6, 2, 1, 1
n = len(arr)
s = sum(range(1,n+1))
from collections import defaultdict
sum_ =  defaultdict(lambda: 0)
for i in arr:
	sum_[i] += 1
	if sum_[i] > 1:
		extra = i
	else:
		s -= i
print(s,extra)

