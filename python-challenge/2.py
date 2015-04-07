f=open('2.txt')
freq={}
lets=[]
for line in f.readlines():
	for letter in line:
		if letter in freq:
			letter_freq=freq[letter]+1
			freq[letter]=letter_freq
		else:	
			lets.append(letter)
			freq[letter]=1
	

for key,value in freq.items():
	print key,value

print lets
