from graph import graph

graph_dict ={
			'b c d' : ['b','c','d','a'],
			'b c' : ['b','c','e'],
			'a' : ['f'],
			'f' : ['g'],
			'c' : ['d'],
			'b' : [],
			'e' : [],
			'd' : [],
			'g' : [],

		}
		
g = graph()
g.set_graph(graph_dict)
g.print_graph()

g.keys()