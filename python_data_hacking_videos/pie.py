import csv
f = open('/home/makala/Downloads/LearnPyData/LearnPyData/data/food.csv')
food_data = csv.DictReader(f)

possible_values = {}


def get_all_possible_values():
	sample = food_data.next()
	keys = sample.keys()
	f.seek(0)
	for key in keys:
		l = list(set([row[key] for row in food_data]))
		possible_values[key] = l
		f.seek(0)
	for key, value in possible_values.items():
		print key,":",value 	

def distinct_values(key):
	l = list(set([row[key] for row in food_data]))
	f.seek(0)
	# print l
	return l

def print_all_keys():
	sample = food_data.next()
	f.seek(0)
	for key in sample.keys():
		print key


# this plots  a pie chart for all the places depending upon the results - (pass, fail , pass w/ conditions)
def results_pie():
	valid_places = [row for row in food_data if 'No' not in row['Results'] and 'Not' not in row['Results'] and 'Out' not in row['Results']]
	total = len(valid_places)
	count ={}
	for place in valid_places:
		res = place['Results']
		if res not in count.keys():
			count[res] = 1
		else:
			count[res] += 1

	for key,value in count.items():
		print key,value
	pie_parts=[]
	labels = []
	for key, value in count.items():
		labels.append(key)
		pie_parts.append(value)


	import pylab
	pylab.pie(pie_parts, labels=labels, autopct='%0.1f%%')
	pylab.show()

from itertools import groupby
# top 5 most violated food places to eat
def violations_pie():
	valid_places = [row for row in food_data if row['Violations'] !='' and 'No' not in row['Results'] and 'Not' not in row['Results'] and 'Out' not in row['Results']]
	problems = {}
	valid_places.sort(key =lambda r: r['DBA Name'])
	places_group = groupby(valid_places, key =lambda r: r['DBA Name'])
	for place,group in places_group:
		all_viols =""
		for row in group:
			all_viols += row['Violations']+'|'
		l = all_viols.split('|')
		l=[item.strip() for item in l]
		problems[place] = len(l)

	import operator
	sorted_list= sorted(problems.items(), key= operator.itemgetter(1), reverse=True )
	sorted_list =sorted_list[:5]
	print type(sorted_list)
	pie_parts=[]
	labels = []
	for item in sorted_list:
		labels.append(item[0])
		pie_parts.append(item[1])
	import pylab
	pylab.pie(pie_parts, labels=labels, autopct='%0.1f%%')
	pylab.show()


	
	

# results_pie()
violations_pie()
# print_all_keys()
