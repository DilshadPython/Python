import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python search_song.py song_name")

# this is apple library link https://itunes.apple.com/search?entity=song&limit=1&term=love

display = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + (sys.argv[1]))
# Befor importing the json library python will change the results from json file to dict
# print(display.json())
# run python search_song.py love

# after adding import json library
print(json.dumps(display.json(), indent=4))
