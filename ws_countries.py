import requests
from bs4 import BeautifulSoup

url="http://www.listofcountriesoftheworld.com/"
r=requests.get(url)
while r.status_code !=200:
	r=requests.get(url)
soup= BeautifulSoup(r.content)
all_divs=soup.find_all("div")
countries=[]
for div in all_divs:
	if div.get("id") == "ctry":
		countries.append((div.text).strip())
cnt=0;


print len(countries)

print "*"+((countries[1].encode("utf-8")).lower()).strip()+"*"
for country in countries:
	if ((country.encode("utf-8")).lower()).strip()=='afghanistan':
		break
	else:
		cnt=cnt+1
print cnt

for i in range(0,cnt):
	countries.remove(countries[0])

for country in countries:
	print country
# cnt=0
# for item in countries:
# 	if item  != 'Afghanistan':
# 		cnt=cnt+1

# print cnt