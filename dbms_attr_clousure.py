
# class list_key:
# 	l=[]
# 	def __init__(self,li):
# 		self.l=li
# 	def get_list(self):
# 		return self.l


class graph:
	graph_dict={}
	visited=[]

	def prepare(self):
		self.graph_dict={
			'ssn pnumber' : ['ssn', 'pnumber', 'hours'],
			'ename' : [],
			'plocation' : [],
			'hours' : [],
			'ssn' : ['ename'],
			'pname' : [],
			'pnumber' : ['plocation', 'pname'],

		}
	def create(self):
		n=int(raw_input("Enter how many nodes\n"))
		for i in range(0,n):
			l=raw_input("\nenter left side of fd with spaces\n")
			# l_obj=list_key(l)
			r=raw_input("enter right side of fd with spaces\n").split()
			self.graph_dict[l]=r

	def print_graph(self):
		for key in self.graph_dict.keys():
			print key, '->', self.graph_dict[key]

	def dfs(self,s):
		print s,","
		self.visited.append(s)
		for value in self.graph_dict[s]:
			if value not in self.visited:
				self.dfs(value)


if __name__ =='__main__':
	fd= graph()
	# fd.prepare()
	fd.create()
	fd.print_graph()
	print "\n"
	for key in fd.graph_dict.keys():
		print "closure of",key,"is--------------"
		fd.dfs(key)
		fd.visited=[]
		print "---------------------------------"

	



# 7
# ssn
# ename
# ename

# pnumber
# plocation pname
# plocation

# ssn pnumber
# ssn pnumber hours
# pname

# hours


