import urllib.parse
import urllib.request as ur
#To build url
def url_builder(artist, song):
    getVars = {'artist' : '', 'song':''}
    getVars['artist'] = artist
    getVars['song'] = song
    url = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?'
    url = url + urllib.parse.urlencode(getVars)
    return url
#Fetches the lyric and returns the xml
def fetch_lyrics(artist, song):
    request = ur.urlopen(url_builder(artist, song))
    response = request.read()
    xml = response.decode("utf-8")
    return xml
#Parses the xml and then returns the 
def parser(xml, tag):
    tag = '<'+ tag + '>'
    index = xml.find(tag)
    #If the index is -1, it means that the <Lyric> tag is not found, So the lyric does not exist:
    if index == -1:
        return "Song not found!"
    else:
        lyric = xml[index+7 : len(xml) - 27]
        return lyric