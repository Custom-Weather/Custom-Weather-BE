from flask import Flask, render_template, request
from datetime import date
import datetime
import time
import requests
import json
import bs4
import random
import events_api
import book_webscrape
import movie_webscraper
import os
import base64
from decouple import config
import pytz
from tzwhere import tzwhere
from dateutil.tz import gettz

app = Flask(__name__)

@app.route('/weather/api/v1/<lat>&<long>', methods=['GET'])

def weather(lat, long):
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

    weather_token = config('WEATHER_API_KEY')
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+long+'&appid='+weather_token+'&units=imperial')
    weather_json = weather_request.json()

    spotify_search = weather_json['current']['weather'][0]['main']

    spotify_get_url = 'https://api.spotify.com/v1/search?q='+spotify_search+',day&type=playlist&limit=1'

    payload = {}
    headers = {
      'Authorization': 'Bearer '+spotify_token+''
    }

    spotify_request = requests.request("GET", spotify_get_url, headers=headers, data = payload)
    spotify_json = spotify_request.json()

    tz = tzwhere.tzwhere()
    local_time_zone = tz.tzNameAt(float(lat), float(long))

    datetime.datetime.fromtimestamp(weather_json['current']['sunrise'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0')

    if weather_json['daily'][0]['temp']['day'] > 60 and (weather_json['current']['weather'][0]['main'] == "Clear" or weather_json['current']['weather'][0]['main'] == "Clouds"):

        five_events = events_api.getEvents(lat, long)
        final = {
                'current': str(weather_json['current']['temp']) + '°F',
                'sunrise': datetime.datetime.fromtimestamp(weather_json['current']['sunrise'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                'sunset': datetime.datetime.fromtimestamp(weather_json['current']['sunset'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                'high': str(weather_json['daily'][0]['temp']['max']) + '°F',
                'low': str(weather_json['daily'][0]['temp']['min']) + '°F',
                'desc': weather_json['current']['weather'][0]['main'],
                'hourly':
                    [{
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][0]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][0]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][0]['weather'][0]['main'],
                        'description': weather_json['hourly'][0]['weather'][0]['description'],
                        'icon': weather_json['hourly'][0]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][1]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][1]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][1]['weather'][0]['main'],
                        'description': weather_json['hourly'][1]['weather'][0]['description'],
                        'icon': weather_json['hourly'][1]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][2]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][2]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][2]['weather'][0]['main'],
                        'description': weather_json['hourly'][2]['weather'][0]['description'],
                        'icon': weather_json['hourly'][2]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][3]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][3]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][3]['weather'][0]['main'],
                        'description': weather_json['hourly'][3]['weather'][0]['description'],
                        'icon': weather_json['hourly'][3]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][4]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][4]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][4]['weather'][0]['main'],
                        'description': weather_json['hourly'][4]['weather'][0]['description'],
                        'icon': weather_json['hourly'][4]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][5]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][5]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][5]['weather'][0]['main'],
                        'description': weather_json['hourly'][5]['weather'][0]['description'],
                        'icon': weather_json['hourly'][5]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][6]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][6]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][6]['weather'][0]['main'],
                        'description': weather_json['hourly'][6]['weather'][0]['description'],
                        'icon': weather_json['hourly'][6]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][7]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][7]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][7]['weather'][0]['main'],
                        'description': weather_json['hourly'][7]['weather'][0]['description'],
                        'icon': weather_json['hourly'][7]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][8]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][8]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][8]['weather'][0]['main'],
                        'description': weather_json['hourly'][8]['weather'][0]['description'],
                        'icon': weather_json['hourly'][8]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][9]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][9]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][9]['weather'][0]['main'],
                        'description': weather_json['hourly'][9]['weather'][0]['description'],
                        'icon': weather_json['hourly'][9]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][10]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][10]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][10]['weather'][0]['main'],
                        'description': weather_json['hourly'][10]['weather'][0]['description'],
                        'icon': weather_json['hourly'][10]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][11]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][11]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][11]['weather'][0]['main'],
                        'description': weather_json['hourly'][11]['weather'][0]['description'],
                        'icon': weather_json['hourly'][11]['weather'][0]['icon']
                        }],
                    }],
                'notifications':
                    five_events,
                'spotify': spotify_json['playlists']['items'][0]['id']
                }

        final_json = json.dumps(final)
        return final_json

    else:
        books = book_webscrape.getBooks()
        random_movies = movie_webscraper.getMovies()
        final = {
                'current': str(weather_json['current']['temp']) + '°F',
                'sunrise': datetime.datetime.fromtimestamp(weather_json['current']['sunrise'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                'sunset': datetime.datetime.fromtimestamp(weather_json['current']['sunset'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                'high': str(weather_json['daily'][0]['temp']['max']) + '°F',
                'low': str(weather_json['daily'][0]['temp']['min']) + '°F',
                'desc': weather_json['current']['weather'][0]['main'],
                'hourly':
                    [{
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][0]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][0]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][0]['weather'][0]['main'],
                        'description': weather_json['hourly'][0]['weather'][0]['description'],
                        'icon': weather_json['hourly'][0]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][1]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][1]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][1]['weather'][0]['main'],
                        'description': weather_json['hourly'][1]['weather'][0]['description'],
                        'icon': weather_json['hourly'][1]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][2]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][2]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][2]['weather'][0]['main'],
                        'description': weather_json['hourly'][2]['weather'][0]['description'],
                        'icon': weather_json['hourly'][2]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][3]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][3]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][3]['weather'][0]['main'],
                        'description': weather_json['hourly'][3]['weather'][0]['description'],
                        'icon': weather_json['hourly'][3]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][4]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][4]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][4]['weather'][0]['main'],
                        'description': weather_json['hourly'][4]['weather'][0]['description'],
                        'icon': weather_json['hourly'][4]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][5]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][5]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][5]['weather'][0]['main'],
                        'description': weather_json['hourly'][5]['weather'][0]['description'],
                        'icon': weather_json['hourly'][5]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][6]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][6]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][6]['weather'][0]['main'],
                        'description': weather_json['hourly'][6]['weather'][0]['description'],
                        'icon': weather_json['hourly'][6]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][7]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][7]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][7]['weather'][0]['main'],
                        'description': weather_json['hourly'][7]['weather'][0]['description'],
                        'icon': weather_json['hourly'][7]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][8]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][8]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][8]['weather'][0]['main'],
                        'description': weather_json['hourly'][8]['weather'][0]['description'],
                        'icon': weather_json['hourly'][8]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][9]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][9]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][9]['weather'][0]['main'],
                        'description': weather_json['hourly'][9]['weather'][0]['description'],
                        'icon': weather_json['hourly'][9]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][10]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][10]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][10]['weather'][0]['main'],
                        'description': weather_json['hourly'][10]['weather'][0]['description'],
                        'icon': weather_json['hourly'][10]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][11]['dt'], gettz(local_time_zone)).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][11]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][11]['weather'][0]['main'],
                        'description': weather_json['hourly'][11]['weather'][0]['description'],
                        'icon': weather_json['hourly'][11]['weather'][0]['icon']
                        }],
                    }],
                'notifications':
                    {
                    'books':
                        books,
                    'movies':
                        random_movies
                    },
                'spotify': spotify_json['playlists']['items'][0]['id']
                }

        final_json = json.dumps(final)
        return final_json

if __name__ == "__main__":
    app.run(debug=True)
