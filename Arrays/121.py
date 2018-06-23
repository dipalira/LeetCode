prices = [7,6,4,3,1]
profit = 0
max_,min_,max_i,min_i = 0,prices[0],0,0
for i,p in enumerate(prices):
	if  max_ < p and i >max_i and i > min_i:
		max_ = p
		max_i = i
	if min_i <i and min_ > p :
		print(p)
		min_ = p
		min_i = i
if min_ > max_:
	min_ = 0
print(max_, min_)