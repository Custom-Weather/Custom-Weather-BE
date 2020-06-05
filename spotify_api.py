import base64
import requests
import json
from decouple import config

def get_spotify(weather_description):
    spotify_id = config('SPOTIFY_CLIENT_ID')
    spotify_secret = config('SPOTIFY_CLIENT_SECRET')

    userpass = spotify_id + ':' + spotify_secret
    encoded_u = base64.b64encode(userpass.encode()).decode()

    spotify_url = "https://accounts.spotify.com/api/token"

    payload = 'grant_type=client_credentials'
    headers = {
      'Authorization': "Basic %s" % encoded_u,
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    spotify_response = requests.request("POST", spotify_url, headers=headers, data = payload)
    spotify_token = (spotify_response.text.encode('utf8'))

    spotify_token_json = json.loads(spotify_token)
    spotify_token_json['access_token']
    spotify_token = spotify_token_json['access_token']

    spotify_get_url = 'https://api.spotify.com/v1/search?q='+weather_description+',day&type=playlist&limit=1'

    payload = {}
    headers = {
      'Authorization': 'Bearer '+spotify_token+''
    }

    spotify_request = requests.request("GET", spotify_get_url, headers=headers, data = payload)
    spotify_json = spotify_request.json()

    return spotify_json
