import requests

proxies = {
	  "http": "http://172.30.0.20:3128",
	  "https": "http://172.30.0.20:3128",
	}

payload = {
    'identity': 'username',
    'password': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    s.post('http://wsdc.nitw.ac.in/student/auth/login', data=payload,proxies=proxies)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print s.text

    # An authorised request.
    r = s.get('http://wsdc.nitw.ac.in/student/attendance/even_sem14_15',proxies=proxies)
    print r.text
