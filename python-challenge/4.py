import requests
from bs4 import BeautifulSoup
nothing=12345
# nothing=66831

proxies = {
	  "http": "http://172.30.0.7:3128",
	  "https": "http://172.30.0.7:3128",
	}
number=1
while(True):
	url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(nothing)
	r=requests.get(url, proxies=proxies)
	while r.status_code is not 200:
		r=requests.get(url, proxies=proxies)
	text=r.text
	number="".join(filter(lambda x: x.isdigit(), text.split()))
	number=number.strip()
	print text
	print "this"+number+"this"
	if 'divide by two' in text.lower():
		nothing=(int(nothing))/2
		continue
	if not number:
		break
	nothing=number
	
# 9386795607