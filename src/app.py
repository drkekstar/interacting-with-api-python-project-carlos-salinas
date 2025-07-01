import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#esto lo que hace es pasarle nuestras credenciales a la API de Spotify
# y nos permite hacer peticiones a la API de Spotify

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# 76R7k5vuX8M7vBDv21DPCv TERE
# 5GGJosGMs08YEmKTZJe1fL Suki waterhouse

#obtener las mejores cacniones del artista
results = spotify.artist_top_tracks("76R7k5vuX8M7vBDv21DPCv")

songs = []
for track in results ['tracks']:
    songs.append({"name": track['name'], 
                  "popularity": track['popularity'], 
                  "duration_min": track['duration_ms']/60000})
df = pd.DataFrame(songs)

print(df)