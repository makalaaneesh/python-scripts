# from a table of(personid,friendid) assuming no cycles it prints a chain of friends greater than 3
import MySQLdb

connection=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="test1")
cursor=connection.cursor()
cursor.execute('select * from friend')


def friend_of(pid):
	l=[]
	for item in list:
		if item[0]==pid:
			l.append(item[1])
	return l

def func(pid,cnt,chain_str):
	chain_str=chain_str+str(pid)+","
	#print chain_str,cnt
	cnt=cnt+1
	l=friend_of(pid)
	cntr=0
	for friend in l:
		func(friend,cnt,chain_str)
		cntr=cntr+1
	if cntr==0 and cnt>3:
		print chain_str
	

list=[]
for row in cursor.fetchall():
	list.append([row[0],row[1]])

for item in list:
	print item[0], ' and his friend is ', friend_of(item[0])
 
for item in list:
	func(item[0],0,'')




