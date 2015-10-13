

import requests
payload = {
    'identity': 'username',
    'password': 'x'
}
from subprocess import call
while(True):
	with requests.Session() as s:
		s.mount("http://", requests.adapters.HTTPAdapter(max_retries=100))
		s.mount("https://", requests.adapters.HTTPAdapter(max_retries=100))
		s.post('http://wsdc.nitw.ac.in/student/auth/login', data=payload)
		r = s.get('http://wsdc.nitw.ac.in/student/hostels/rules')
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(r.content)
		main_div = soup.find("div", {"id": "schedule"})
		if 'coming soon!!' not in main_div.text:
			call("vlc /home/makala/Desktop/ultra15.mp3", shell=True)
			break
		else:
			print False
