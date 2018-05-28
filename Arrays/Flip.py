x = [[1,1,0],[1,0,1],[0,0,0]]
output = []
for ele in x:
	t = []
	for e in reversed(ele):
		if e == 1:
			t.append(0)
		else:
			t.append(1)
	output.append(t)
print(output)
