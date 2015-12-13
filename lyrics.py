import requests
from xml.dom import minidom
from bs4 import BeautifulSoup

def getXML(track, artist):
	url = "http://lyrics.wikia.com/api.php?action=lyrics&artist="+artist+"&song="+track+"&fmt=xml"
	r = requests.get(url)
	content = r.content
	return content


def getURL(xml_string):
	xmldoc = minidom.parseString(xml_string)
	itemlist = xmldoc.getElementsByTagName('url')
	url =  itemlist[0].firstChild.nodeValue
	return url


def getLyrics(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	divs = soup.find_all("div", { "class" : "lyricbox" })
	if(len(divs) == 0):
		print "NO LYRICS FOUND"
		return
	l = divs[0].contents
	lyrics_unrefined =  l[1:len(l)-5]
	lyrics_refined = [lyric.encode('utf-8') for lyric in lyrics_unrefined if '<br' not in lyric.encode('utf-8')]
	return  "\n".join(lyrics_refined)

if __name__ == "__main__":
	track = "can't get enough" # track name 
	artist = "j cole" # artist. ( only the main aritst )
	xml = getXML(track,artist)
	url = getURL(xml)
	lyrics = getLyrics(url)
	print lyrics