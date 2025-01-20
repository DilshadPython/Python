import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python search_song.py song_name")

# this is apple library link https://itunes.apple.com/search?entity=song&limit=20&term=love
# searching for 25 song have the love word return with trackname results, limit=25
display = requests.get('https://itunes.apple.com/search?entity=song&limit=25&term=' + (sys.argv[1]))

# Now we are search for the trackName in the library because love song has other name check to find
# run python find_name.py love
name = display.json()
for output in name['results']:
    print('Find output of the love song  >>> ' + output['trackName'])
