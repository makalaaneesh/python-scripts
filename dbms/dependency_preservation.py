from graph import *
graph_dict={
	'a':['d'],
	'b':['e'],
	'd e':['d','e','c'],
	'c':[],
	'd':[],
	'e':[]
}

g = graph()
g.set_graph(graph_dict)
g.print_graph()

# for key in g.graph_dict.keys():
# 	g.closure(key)
# g.closure('a b')
# g.closure('b c')
# g.closure('a c')
# g.closure('a b c')

# dec = ['a','b','c']
# import itertools
# p = itertools.combinations(dec,2)
# p_list = list(p)
# for item in p_list:
# 	print '.'+(" ".join(item)).strip()+"."

s = decomposed_graph()
s.gen_decomposed_graph(g)
s.print_graph()