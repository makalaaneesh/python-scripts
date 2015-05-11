import itertools
class graph:
	"""A class to implement algorithms pertaining to dbms"""
	graph_dict = {}
	visited = []
	def set_graph(self, g):
		self.graph_dict=g
	def has_multiple_attributes(self,vertex):
		return True if ' ' in vertex else False
		
	def create_graph(self):
		print "YOU HAVE TO ENTER EACH FUNCTIONAL DEPENDENCY GIVING A SPACE WHEN SPECIFYING MULTIPLE ATTRIBUTES IN ALPHABETICAL ORDER"
		v = int(raw_input("Enter no of vertices\n"))
		for i in range(v):
			vertex = raw_input("Enter the left side of the fd\n")
			edges = raw_input("Enter the right side of the fd\n").split()	
			if self.has_multiple_attributes(vertex):
				edges = edges + [ver for ver in vertex.split()]		
			self.graph_dict[vertex] = edges
			print "..."


	def print_graph(self):
		print '\nPrinting the graph....................'
		for key, value in self.graph_dict.items():
			print key," : ", value	
		print '......................................\n'

	def keys(self):
		keys = []
		attrs = [x for x in self.graph_dict.keys() if not self.has_multiple_attributes(x)]
		no_of_keys = len(attrs)
		for i in range(1,no_of_keys):
			p = itertools.combinations(attrs,i)
			for permutation in p:
				possible_key = " ".join(permutation)
				if len(self.closure2(possible_key)) == no_of_keys:
					keys.append("".join(possible_key.split()))
		print "keys are ", keys
		print "primary key is ", keys[0]

	def depth_first_search(self, vertex):
		if vertex in self.visited:
			return
		self.visited.append(vertex)
		# print vertex,' , ',
		for edge in self.graph_dict[vertex]:
			if edge not in self.visited:
				self.depth_first_search(edge)

	def closure(self, vertex):
		# print "\nClosure of ",vertex,":"
		self.visited = []
		if self.has_multiple_attributes(vertex):
			if vertex in self.graph_dict.keys():
				self.depth_first_search(vertex)
			# print 'multiple'
			for attr in vertex.split():
				self.depth_first_search(attr)
			added = True
			while(True):
				added = False
				for key in self.graph_dict.keys():
					if self.has_multiple_attributes(key) and set(key.split()).issubset(set(self.visited)):
						# print "enterd"
						v_count =len(self.visited)
						self.depth_first_search(key)
						if len(self.visited) > v_count:
							added = True
				if not added:
					break
			temp = filter(lambda x: not self.has_multiple_attributes(x) ,list(set(self.visited))) 
			self.visited = []
			# print temp
			return temp
		else:
			self.depth_first_search(vertex)
			print self.visited
			temp=self.visited
			self.visited = []
			return temp
	# closure2 is the improved function that supports closure of an attribute or a set of attributes
	def closure2(self,vertex):
		self.visited = []
		for attr in vertex.split():
			self.depth_first_search(attr)
		added = True
		while(True):
			added = False
			for key in self.graph_dict.keys():
				if self.has_multiple_attributes(key) and set(key.split()).issubset(set(self.visited)):
					# print "enterd"
					v_count =len(self.visited)
					self.depth_first_search(key)
					if len(self.visited) > v_count:
						added = True
			if not added:
				break
		temp = filter(lambda x: not self.has_multiple_attributes(x) ,list(set(self.visited))) 
		self.visited = []
		# print temp
		return temp	

class decomposed_graph(graph):
	def gen_decomposed_graph(self, g_d):
		self.graph_dict={}
		vertices = raw_input("\nenter the various attributes of the decomposed realtion").split()
		for vertex in vertices:
			self.graph_dict[vertex] = [item for item in g_d.closure(vertex) if item in vertices and item is not vertex]
		# for key in g_d.graph_dict.keys():
		# 	all_present = True
		# 	for attr in key.split():
		# 		if attr not in vertices:
		# 			all_present= False
		# 			break
		# 	if all_present:
		# 		self.graph_dict[key] = [item for item in g_d.graph_dict[key] if item in vertices]
		import itertools
		for i in range(1, len(vertices)+1):
			p = itertools.combinations(set(vertices),i)
			p_list = list(p)
			for item in p_list:
				attr= " ".join(sorted(item))
				value_list = [item for item in g_d.closure(attr) if item in vertices and item not in attr.split()]
				if value_list:
					self.graph_dict[attr] = value_list



