import urllib.request as ur
import urllib.parse
import json
import xml.etree.ElementTree as etree
def url_builder(artist, song):
    getVars = {'artist' : '', 'song':''}
    getVars['artist'] = artist
    getVars['song'] = song
    url = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?'
    url = url + urllib.parse.urlencode(getVars)
    return url
request = ur.urlopen(url_builder('metallica', 'unforgiven'))
response = request.read()
xml = response.decode("utf-8")
def parser(xml, tag):
    tag = '<'+ tag + '>'
    index = xml.find(tag)
    lyric = xml[index+7 : len(xml) - 27]
    return lyric
lyric = parser (xml, "Lyric")
print(lyric)