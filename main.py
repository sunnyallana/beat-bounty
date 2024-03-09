#Required Libraries and Modules
from dotenv import load_dotenv
from pytube import YouTube, Search
import os
import requests
import json
import base64

#Load the environment variables
load_dotenv()
#Get the environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#Get Token
def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    base64_bytes = str(base64.b64encode(auth_bytes), 'utf-8')
    url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': f'Basic {base64_bytes}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {"grant_type": "client_credentials"}    

    response = requests.post(url, headers=headers, data=payload)
    response_json = json.loads(response.content)
    token = response_json['access_token']
    return token

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def search_artist(artist_name, token):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.content)['artists']['items']
    if len(response_json) > 0:
        return response_json[0]
    else:
        return None

def get_songs_by_artist(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.content)['tracks']
    return response_json


def get_video_url(query):
    # Perform a search on YouTube
    search_results = Search(query)
    url = f"https://www.youtube.com/watch?v={search_results.results[0].video_id}"
    print(url)
    return url

def download_music_mp3(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            out_file = audio_stream.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            print("Download completed successfully!")
        else:
            print("No audio stream found for the provided URL.")
    except Exception as e:
        print("\nSomething Went Wrong:", e, "\n")



def main():
    #Get the token
    token = get_token()
    artist_name = input("Enter artist's name: ")
    response = search_artist(artist_name, token)
    artist_id = response['id']
    songs = get_songs_by_artist(artist_id, token)

    #Print the songs
    for song in songs:
        print(song['name'])
        url = get_video_url(f"{song['name']}" + " by " + f"{artist_name}" )
        download_music_mp3(url)
