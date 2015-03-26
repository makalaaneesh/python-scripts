import requests
import json



email="makalaaneesh@yahoo.com"
url="https://api.fullcontact.com/v2/person.json?email="+email+"&apiKey=18167323494eab42"
print url

r=requests.get(url)
json_loaded = json.loads(r.text)
print type(json_loaded)
print json_loaded.keys()
for key in json_loaded.keys():
	print key, ":", json_loaded[key]
