
from __future__ import division
import requests
import sys



url = "http://www.mp3pulse.ru/uploads/files/muz/Justin_Bieber_-_What_Do_You_Mean_(Jerome_Price_Club_Mix)_[www.mp3pulse.ru].mp3"
size = 0
lower = 0 
chunkSize = 1000000 #in bytes the chunksize to divide the file into
proxies = {
	  "http": "http://172.30.0.13:3128",
	  "https": "http://172.30.0.13:3128",
	}

filename = url.split('/')[-1]

if '.' not in filename:
	extension = raw_input("Enter file extension eg: \".mp3\"")
	filename = "file"+extension
with open(filename,'wb')as f:
	while True:
		r = requests.get(url, stream = True,headers = {'Range': 'bytes='+str(lower)+'-'+str(lower+chunkSize)}, proxies = proxies)
		print r.status_code
		if r.status_code != 206: # 206 is the status code for partial content
			print 'breaking'
			break
		for chunk in r.iter_content(chunk_size = 1024): #to download the file as a stream to speed up things
			if chunk:
				f.write(chunk)
				size = size + 1024
				to_print =  str(size/1000000) + ' mb downloaded'
				sys.stdout.write('\r'+to_print)
		
		
		lower = lower + chunkSize

print filename, "completed downloading"

