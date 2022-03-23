# Shows the top tracks for a user (code runs on local PC, not on lab PCs - localhost didn't send any data)

import pandas as pd
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'
username = 'isamusical1'
client_id = 'a0c0005784b54ec9bfa4b046d7548c19'
client_secret = '715ed7be535b489c9f44e29398a1e7a7'
redirect_uri = 'http://localhost:8080'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)
ranges = ['short_term', 'medium_term', 'long_term']
song = pd.DataFrame()

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
      
    print()
    
#TODO: Covert JSON to dataframe - Monday at the latest
#TODO: Add CSV file or other - Monday at the latest
#TODO: Add basic GUI (Tkinter) - Thursday

song.add(results)
    # playlists = sp.user_playlists('spotify')
    
# playlist = sp.user_playlist_tracks('spotify', 'isamusical1')
# songs = playlist['items']

#df = pd.DataFrame(songs)

 # df.to_csv('Songs.csv', sep=';', encoding= 'utf-8', index=True)
    
# while playlists:
 #   for i, playlist in enumerate(playlists['items']):
  #      print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
   # if playlists['next']:
    #    playlists = sp.next(playlists)
    # else:
    #  playlists = None