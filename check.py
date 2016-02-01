from datetime import datetime
import time
import requests
import threading
import json


class ProxyChecker(threading.Thread):
	def __init__(self, address, port, _dict, url):
		threading.Thread.__init__(self)
		self.address = address
		self.port = port
		self.l = _dict
		self.url = url
		self.proxies = {
			"http": "http://"+address+":"+port,
			"https": "http://"+address+":"+port,
		}

	def run(self):
		a="port:"+self.port+" "+ self.address
		time1 = time.time()
		time2=time1
		try:
			r=requests.get("http://"+self.url, proxies=self.proxies, timeout=10)
			time2 = time.time()

		except requests.exceptions.ConnectTimeout as e:
			print a, "-Connection Timeout"
		except requests.exceptions.ReadTimeout as e:
			print a, "-Read Timeout"
		except requests.exceptions.ConnectionError as e:
			print a, "-ConnectionError"
		else:
			if r.status_code==200:
				self.l.update({time2-time1:a})
				# x[a]=str(time2-time1)
				# results.append(a)
				print a, "-Working"+"in seconds-"+str(time2-time1)
			else:
				print a, "-Not Working"



def get_proxy_times(sub_ip_list, port_list, start, end, url):
	l={}
	threads = []
	results = []
	to_return = {}
	for port in ports:
		for n in ipl:
			for x in range(start,end):
				proxy_address = "172."+n+".0."+str(x)
				thread = ProxyChecker(proxy_address, port, l ,url)
				thread.start()
				threads.append(thread)

	for t in threads:
		t.join()

	print"---------------------------------------"
	print"       Proxies it works in are:"
	print"---------------------------------------"

	for item in sorted(l.keys()):
		to_return[l[item]] = item
		print l[item]+"-   "+str(item)
	return to_return


if __name__ == "__main__":		
	ipl = ['30']
	ports = ['3128']
	start = 7
	end = 27
	url=raw_input("enter the url to check which on which proxies this website will run\n")
	result = get_proxy_times(ipl, ports, start,end, url)
	with open('proxies.txt', 'w') as outfile:
		json.dump(result, outfile)