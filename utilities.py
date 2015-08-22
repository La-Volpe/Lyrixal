import urllib.parse
import urllib.request as ur
import demjson as json
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
        return "Song not found!\nTry:\n/find [Artist Name] - [Song Name]\nfor a better result."
    else:
        lyric = xml[index+7 : - 27]
        return lyric
#---------------------------------------------------------------
#builds the link to lyrics wikia...
def wikia_url_builder(artist, song):
    getVars = {'func':'getSong','artist' : '', 'song':'','fmt':'json'}
    getVars['artist'] = artist
    getVars['song'] = song
    url = 'http://lyrics.wikia.com/api.php?'
    url = url + urllib.parse.urlencode(getVars)
    return url
#Fetches the preview and the link to lyrics wikia...
def fetch_from_wiki(artist, song):
    url = wikia_url_builder(artist, song)
    request = ur.urlopen(url).read().decode('utf-8')
    request = request[7:len(request)]
    _json = json.decode(request)
    return _json
#Prepares the proper response:
def response(fetched):
    lyric = fetched['lyrics']
    if lyric == "Not found":
        return "Lyrics not found!"
    else:
        url = fetched['url']
        resp = lyric+"\n"+url
        return resp
#song = fetch('Brendan Perry', 'crescent')
#resp = response(song)
