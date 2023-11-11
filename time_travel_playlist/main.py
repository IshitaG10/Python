import requests
import os
from dotenv import find_dotenv,load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_PATH = os.getenv("SPOTIFY_REDIRECT_PATH")
URL = "https://www.billboard.com/charts/hot-100"



# scraping billboard website
date = input("Which day do you want to travel to? Type your date in YYYY-MM-DD format:\n")

response = requests.get(url=f"{URL}/{date}")
content  = response.text

billboard_web_page = BeautifulSoup(content,"html.parser")
all_songs = billboard_web_page.select(selector="li h3", class_="c-title")
titles = [(title.getText()).strip("\n\t") for title in all_songs ]
song_titles = titles[0:100]


#spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31yercipzoqr5cwfov2sqqwwxb6e", 
    )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]

songs = []
for song in song_titles:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        songs.append(uri)
    except IndexError:
        continue

PLAYLIST_ID = sp.user_playlist_create(user=user_id,public=False,name=f"{date} BillBoard-100")['id']
sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=songs,user=user_id)
print("Playlist Created")