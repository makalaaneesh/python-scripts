office_lat = 41.980262
office_lon = -87.668452


from xml.etree.ElementTree import parse
doc = parse('rt22.xml')
for bus in doc.findall('bus'):
	lat = bus.findtext('lat')
	lon = bus.findtext('lon')
	id = bus.findtext('id')
	dire = bus.findtext('d').lower()

	lat = float(lat)
	if lat > office_lat and 'north' in dire:
		print id, lat, dire
		# # url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+str(lat)+","+lon
		# url = "http://google.com/maps/place/?z=12&t=m&q=loc:@58.698017, -152.522067"
		# import webbrowser
		# webbrowser.open(url)


