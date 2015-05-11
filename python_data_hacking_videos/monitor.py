office_lat = 41.980262
office_lon = -87.668452


buses = ['4063']
import requests
import urllib
import time

while True:
	r = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
	from xml.etree.ElementTree import parse
	# f = open('rt22.xml', 'wb')
	# f.write(r.text)
	# f.close()
	doc = parse(r)
	for bus in doc.findall('bus'):
		if bus.findtext('id') in buses:
			print bus.findtext('id'), bus.findtext('lat'), ((float(bus.findtext('lat'))-office_lat)*69)
	time.sleep(5)
