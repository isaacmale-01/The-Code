# Shows the top artists for a user (code runs on local PC's, not on lab PC's - see The Program 2)

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

scope = 'user-top-read'
username = ""
client_id = 'a0c0005784b54ec9bfa4b046d7548c19'
client_secret = '715ed7be535b489c9f44e29398a1e7a7'
ranges = ['short_term', 'medium_term', 'long_term']

os.environ['SPOTIPY_CLIENT_ID']= client_id
os.environ['SPOTIPY_CLIENT_SECRET']= client_secret
redirect_uri = 'http://localhost:8000'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Sorry, we can't get the token for", username)


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_artists(limit=50,offset=0,time_range='short_term')
    for song in range(50):
        list = []
        list.append(results)
        with open('top50_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)

with open('top50_data.json') as f:
    data = json.load(f)

list_of_results = data[0]["items"]
list_of_artist_names = []
list_of_artist_uri = []
list_of_genres = []

for result in list_of_results:
    #result[""]
    this_artists_name = result["name"][0]
    list_of_artist_names.append(this_artists_name)
    this_artists_uri = result["uri"][0]
    list_of_artist_uri.append(this_artists_uri)
    this_artists_genre = result["genres"][0]
    list_of_genres.append(this_artists_genre)

    all_genres = pd.DataFrame(
    {'artist': list_of_artist_names,
     'artist_uri': list_of_artist_uri,
     'genres': list_of_genres   
    })

all_genres_saved = all_genres.to_csv('top50_data.csv')


