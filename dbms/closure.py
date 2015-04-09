from graph import graph

graph_dict ={
			'ssn pnumber' : ['ssn', 'pnumber', 'hours'],
			'ename' : [],
			'plocation' : [],
			'hours' : [],
			'ssn' : ['ename'],
			'pname' : [],
			'pnumber' : ['plocation', 'pname'],

		}
		
g = graph()
g.set_graph(graph_dict)
g.print_graph()
for vertex in g.graph_dict.keys():
	g.closure(vertex)
