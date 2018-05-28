adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}




## Non-recursive
def dfs(graph, start):
	"""
	All possible connected vertices
	"""
	stack,path = [start],[]
	while stack:
		ele = stack.pop()
		if ele in path:
			continue
		else:
			path.append(ele)
			for neighbours in graph[ele]:
				stack.append(neighbours)

	return path

print(dfs(adjacency_matrix,1))


def dfs_recur(graph,start,path):

	#print("step", path)
	path.append(start)
	for neighbour in graph[start]:
		print("neighbour",neighbour)
		if neighbour not in path:
			path = dfs_recur(graph,neighbour,path)
	return path
print("recursive",dfs_recur(adjacency_matrix,1,[]))
