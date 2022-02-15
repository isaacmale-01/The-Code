# Shows the top tracks for a user

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'
username = 'isamusical1'
client_id = 'a0c0005784b54ec9bfa4b046d7548c19'
client_secret = '715ed7be535b489c9f44e29398a1e7a7'
redirect_uri = 'http://localhost:8000'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)
ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()

    playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None