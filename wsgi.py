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

app = Flask(__name__)

@app.route('/weather/api/v1/<lat>&<long>', methods=['GET'])

def weather(lat, long):
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+long+'&appid=c5ec3e05ed22c969db668578d373540a&units=imperial')
    weather_json = weather_request.json()

    if weather_json['daily'][0]['temp']['day'] > 0 and (weather_json['current']['weather'][0]['main'] == "Clear" or weather_json['current']['weather'][0]['main'] == "Clouds"):

        five_events = events_api.getEvents(lat, long)
        final = {
                'current': str(weather_json['current']['temp']) + '°F',
                'sunrise': datetime.datetime.fromtimestamp(weather_json['current']['sunrise']).strftime('%I:%M %p').lstrip('0'),
                'sunset': datetime.datetime.fromtimestamp(weather_json['current']['sunset']).strftime('%I:%M %p').lstrip('0'),
                'high': str(weather_json['daily'][0]['temp']['max']) + '°F',
                'low': str(weather_json['daily'][0]['temp']['min']) + '°F',
                'desc': weather_json['current']['weather'][0]['main'],
                'hourly':
                    [{
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][0]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][0]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][0]['weather'][0]['main'],
                        'description': weather_json['hourly'][0]['weather'][0]['description'],
                        'icon': weather_json['hourly'][0]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][1]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][1]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][1]['weather'][0]['main'],
                        'description': weather_json['hourly'][1]['weather'][0]['description'],
                        'icon': weather_json['hourly'][1]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][2]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][2]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][2]['weather'][0]['main'],
                        'description': weather_json['hourly'][2]['weather'][0]['description'],
                        'icon': weather_json['hourly'][2]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][3]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][3]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][3]['weather'][0]['main'],
                        'description': weather_json['hourly'][3]['weather'][0]['description'],
                        'icon': weather_json['hourly'][3]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][4]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][4]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][4]['weather'][0]['main'],
                        'description': weather_json['hourly'][4]['weather'][0]['description'],
                        'icon': weather_json['hourly'][4]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][5]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][5]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][5]['weather'][0]['main'],
                        'description': weather_json['hourly'][5]['weather'][0]['description'],
                        'icon': weather_json['hourly'][5]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][6]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][6]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][6]['weather'][0]['main'],
                        'description': weather_json['hourly'][6]['weather'][0]['description'],
                        'icon': weather_json['hourly'][6]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][7]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][7]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][7]['weather'][0]['main'],
                        'description': weather_json['hourly'][7]['weather'][0]['description'],
                        'icon': weather_json['hourly'][7]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][8]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][8]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][8]['weather'][0]['main'],
                        'description': weather_json['hourly'][8]['weather'][0]['description'],
                        'icon': weather_json['hourly'][8]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][9]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][9]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][9]['weather'][0]['main'],
                        'description': weather_json['hourly'][9]['weather'][0]['description'],
                        'icon': weather_json['hourly'][9]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][10]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][10]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][10]['weather'][0]['main'],
                        'description': weather_json['hourly'][10]['weather'][0]['description'],
                        'icon': weather_json['hourly'][10]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][11]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][11]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][11]['weather'][0]['main'],
                        'description': weather_json['hourly'][11]['weather'][0]['description'],
                        'icon': weather_json['hourly'][11]['weather'][0]['icon']
                        }],
                    }],
                'notifications':
                    five_events
                }
                
        final_json = json.dumps(final)
        return final_json

    else:
        books = book_webscrape.getBooks()
        random_movies = movie_webscraper.getMovies()
        final = {
                'current': str(weather_json['current']['temp']) + '°F',
                'sunrise': datetime.datetime.fromtimestamp(weather_json['current']['sunrise']).strftime('%I:%M %p').lstrip('0'),
                'sunset': datetime.datetime.fromtimestamp(weather_json['current']['sunset']).strftime('%I:%M %p').lstrip('0'),
                'high': str(weather_json['daily'][0]['temp']['max']) + '°F',
                'low': str(weather_json['daily'][0]['temp']['min']) + '°F',
                'desc': weather_json['current']['weather'][0]['main'],
                'hourly':
                    [{
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][0]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][0]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][0]['weather'][0]['main'],
                        'description': weather_json['hourly'][0]['weather'][0]['description'],
                        'icon': weather_json['hourly'][0]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][1]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][1]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][1]['weather'][0]['main'],
                        'description': weather_json['hourly'][1]['weather'][0]['description'],
                        'icon': weather_json['hourly'][1]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][2]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][2]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][2]['weather'][0]['main'],
                        'description': weather_json['hourly'][2]['weather'][0]['description'],
                        'icon': weather_json['hourly'][2]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][3]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][3]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][3]['weather'][0]['main'],
                        'description': weather_json['hourly'][3]['weather'][0]['description'],
                        'icon': weather_json['hourly'][3]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][4]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][4]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][4]['weather'][0]['main'],
                        'description': weather_json['hourly'][4]['weather'][0]['description'],
                        'icon': weather_json['hourly'][4]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][5]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][5]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][5]['weather'][0]['main'],
                        'description': weather_json['hourly'][5]['weather'][0]['description'],
                        'icon': weather_json['hourly'][5]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][6]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][6]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][6]['weather'][0]['main'],
                        'description': weather_json['hourly'][6]['weather'][0]['description'],
                        'icon': weather_json['hourly'][6]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][7]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][7]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][7]['weather'][0]['main'],
                        'description': weather_json['hourly'][7]['weather'][0]['description'],
                        'icon': weather_json['hourly'][7]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][8]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][8]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][8]['weather'][0]['main'],
                        'description': weather_json['hourly'][8]['weather'][0]['description'],
                        'icon': weather_json['hourly'][8]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][9]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][9]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][9]['weather'][0]['main'],
                        'description': weather_json['hourly'][9]['weather'][0]['description'],
                        'icon': weather_json['hourly'][9]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][10]['dt']).strftime('%I:%M %p').lstrip('0'),
                    'temp': str(weather_json['hourly'][10]['temp']) + '°F',
                    'weather':
                        [{
                        'main': weather_json['hourly'][10]['weather'][0]['main'],
                        'description': weather_json['hourly'][10]['weather'][0]['description'],
                        'icon': weather_json['hourly'][10]['weather'][0]['icon']
                        }],
                    },
                    {
                    'dt': datetime.datetime.fromtimestamp(weather_json['hourly'][11]['dt']).strftime('%I:%M %p').lstrip('0'),
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
                    }
                }
        final_json = json.dumps(final)
        return final_json

if __name__ == "__main__":
    app.run(debug=True)
