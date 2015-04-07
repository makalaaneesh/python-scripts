# val="".join([line for line in open('3.txt')])
f=open('3.txt')


# name="ansddkadjaskdakAAAnDDDfaklndkasndkanBBBnCCCkdaldkasld"
import re
# p= re.search('[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]',name)
p= re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')
# p=re.compile('BIG[a-z]BIG')
l=[]
for val in f:
	l=l+(p.findall(val))
# print len(p.findall(val))
print "".join([item[4] for item in l])
