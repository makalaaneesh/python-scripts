graph={
	1:[2,4,5],
	2:[3],
	3:[5],
	4:[],
	5:[2],
	
}

def dfs(node,visited):
	visited.append(node)
	print node
	for edge_node in graph[node]:
		if edge_node not in visited:
			dfs(edge_node, visited)
	
	
def dfs1(check_node,node,visited):
	visited.append(node)
	print node
	for edge_node in graph[node]:
		if edge_node == check_node:
			print 'cyclic'
			return
		else:
			if edge_node not in visited:
				dfs1(check_node,edge_node, visited)


#dfs(1,[])
dfs1(5,5,[])


#9386795607
