import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.alltechbuzz.net/top-best-free-proxy-sites-servers-2015/")
soup = BeautifulSoup(r.content)


mydivs = soup.find_all("div", { "class" : "entry-content" })
li=[]
for div in mydivs:
	li+=div.find_all("li")
aa=[]
for ln in li:
	link = ln.a
	aa.append(link)

links = [item['href'] for item in aa if item is not None]
print links


proxies = {
	  "http": "http://172.30.0.20:3128",
	  "https": "http://172.30.0.20:3128",
	}
ll=[]
for line in links:
	url="http://www."+ line
	re= requests.get(url, proxies=proxies)
	if re.status_code == 200:
		print url
		ll.append(url)
	else:
		print "not wroking ", url

print ll
