# Shows the top tracks for a user from a particular year (in this case 2019) - but code doesn't produce any output?
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'a0c0005784b54ec9bfa4b046d7548c19'
secret = '715ed7be535b489c9f44e29398a1e7a7'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
sp.trace=False


artist_name = []
track_name = []
popularity = []
track_id = [] 

for i in range(0,250,50):
    track_results = sp.search(q='year:2020', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

playlist = sp.user_playlist_tracks('spotify', '')
songs = playlist['items']

df = pd.DataFrame(songs)

df.to_csv('Songs.csv', sep=';', encoding= 'utf-8', index=True)