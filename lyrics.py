#
# Needs work on 
# 1. parsing the main aritst when artist is of the format -"xyz ft. abc"
# 2. support for bad tags
#
import requests
from xml.dom import minidom
from bs4 import BeautifulSoup
import sys
import easygui

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
		return "NO LYRICS FOUND"
	l = divs[0].contents
	lyrics_unrefined =  l[1:len(l)-5]
	lyrics_refined = [lyric.encode('utf-8') for lyric in lyrics_unrefined if '<br' not in lyric.encode('utf-8')]
	return  "\n".join(lyrics_refined)

if __name__ == "__main__":
	# track = "adventure of a lifetime" # track name 
	# artist = "coldplay" # artist. ( only the main aritst )
	if(len(sys.argv) > 3):
		args = sys.argv
		track = "".join(args[1:args.index("|")])
		artist = "".join(args[args.index("|")+1:])
		# print "python", track, artist
		xml = getXML(track,artist)
		url = getURL(xml)
		lyrics = getLyrics(url)
		print lyrics
		easygui.textbox(track+" "+artist,track+" "+artist,lyrics)
	else:
		print "IMPROPER TAGS"
