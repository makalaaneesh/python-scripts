from datetime import datetime
import time
import requests
# a="25"
url=raw_input("enter the url to check which on which proxies this website will run\n")
l={}
for x in range(7,27):
	a=str(x)

	proxies = {
	  "http": "http://172.30.0."+a+":3128",
	  "https": "http://172.30.0."+a+":3128",
	}
	time1 = time.time()
	time2=time1
	try:
		r=requests.get("http://"+url, proxies=proxies, timeout=5)
		# r=requests.get("https://stream.twitter.com/1.1/statuses/filter.json?track=kejriwal", proxies=proxies, timeout=5)
		time2 = time.time()

	except requests.exceptions.ConnectTimeout as e:
		print a+"-Connection Timeout"
	except requests.exceptions.ReadTimeout as e:
		print a+"-Read Timeout"
	except requests.exceptions.ConnectionError as e:
		print a+"-ConnectionError"
	else:
		if r.status_code==200:
			l.update({str(time2-time1):a})
			# x[a]=str(time2-time1)
			print a+"-Working"+"in seconds-"+str(time2-time1)
		else:
			print a+"-Not Working", r.status_code


print"---------------------------------------"
print"       Proxies it works in are:"
print"---------------------------------------"
for item in sorted(l.keys()):
	print l[item]+"-   "+item
# sorted_l = sorted(l.items(), key=operator.itemgetter(1))
# print key for (key, value) in sorted(l.values())


