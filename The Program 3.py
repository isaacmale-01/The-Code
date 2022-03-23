# Shows the top artists for a user (code runs on local PC's, not on lab PC's - see The Program 2)

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

