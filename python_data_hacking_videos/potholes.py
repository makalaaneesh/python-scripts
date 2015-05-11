import csv
f = open('/home/makala/Downloads/LearnPyData/LearnPyData/data/potholes.csv')
r= csv.DictReader(f)
# actions = set([])
block_count={}
for row in r:
	if "Completed" in row['STATUS'] or "Dup" in row['STATUS']:
		continue
	# print row['STATUS']
	if row['STREET ADDRESS'] == 'STREET ADDRESS':
		continue
	add_list = row['STREET ADDRESS'].split()
	if len(add_list) == 0:
		continue
	block_num = add_list[0]
	if block_num.isalpha():
		continue
	add_list[0] = block_num[:-1]+"X"
	if " ".join(add_list) not in block_count:
		block_count[" ".join(add_list)] = 1
	else:
		block_count[" ".join(add_list)] += 1



import operator
sorted_count = sorted(block_count.items(), key=operator.itemgetter(1), reverse = True)

print sorted_count[:5]



