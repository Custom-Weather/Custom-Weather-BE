from flask import Flask, render_template, request
from datetime import date
import datetime
import time
import requests
import json
import bs4
import random

app = Flask(__name__)

@app.route('/weather/api/v1/<lat>&<long>', methods=['GET'])

def weather(lat, long):
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+long+'&appid=c5ec3e05ed22c969db668578d373540a&units=imperial')
    weather_json = weather_request.json()

    if weather_json['daily'][0]['temp']['day'] > 60 and (weather_json['current']['weather'][0]['main'] == "Clear" or weather_json['current']['weather'][0]['main'] == "Clouds"):

        events_request = requests.get('http://api.eventful.com/json/events/search?...&where='+lat+','+long+'&within=20&app_key=pz8fmcjnBKqnM8rw')
        events_json = events_request.json()


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
                    'event_one':
                        {
                        'name': events_json['events']['event'][0]['title'],
                        'url': events_json['events']['event'][0]['url']
                        },
                    'event_two':
                        {
                        'name': events_json['events']['event'][1]['title'],
                        'url': events_json['events']['event'][1]['url']
                        },
                    'event_three':
                        {
                        'name': events_json['events']['event'][2]['title'],
                        'url': events_json['events']['event'][2]['url']
                        },
                    'event_four':
                        {
                        'name': events_json['events']['event'][3]['title'],
                        'url': events_json['events']['event'][3]['url']
                        },
                    'event_five':
                        {
                        'name': events_json['events']['event'][4]['title'],
                        'url': events_json['events']['event'][4]['url']
                        }
                    }
                }

        final_json = json.dumps(final)
        return final_json

    else:

        # def getBooks(url):
        res = requests.get('https://www.goodreads.com/shelf/show/trending')
        res.raise_for_status

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.find_all("a", class_="bookTitle")[0:10]
        books = [i.text for i in elems]

        # def getMovies()
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value')
              for b in soup.select('td.posterColumn span[name=ir]')]
        imdb = []

        # Movie List Creation
        for index in range(0, len(movies)):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index))+1:-7]
            place = movie[:len(str(index))-(len(movie))]
            imdb.append(movie_title)

        random_movies = random.sample(imdb, 10)

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
                        {
                        'book1': f'{books[0]}',
                        'book2': f'{books[1]}',
                        'book3': f'{books[2]}',
                        'book4': f'{books[3]}',
                        'book5': f'{books[4]}',
                        'book6': f'{books[5]}',
                        'book7': f'{books[6]}',
                        'book8': f'{books[7]}',
                        'book9': f'{books[8]}',
                        'book10': f'{books[9]}',
                        },
                    'movies':
                        {
                        'movie1': f'{random_movies[0]}',
                        'movie2': f'{random_movies[1]}',
                        'movie3': f'{random_movies[2]}',
                        'movie4': f'{random_movies[3]}',
                        'movie5': f'{random_movies[4]}',
                        'movie6': f'{random_movies[5]}',
                        'movie7': f'{random_movies[6]}',
                        'movie8': f'{random_movies[7]}',
                        'movie9': f'{random_movies[8]}',
                        'movie10': f'{random_movies[9]}'
                        }
                    }
                }
        final_json = json.dumps(final)
        return final_json


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
