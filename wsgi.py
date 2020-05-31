from flask import Flask, render_template, request
from datetime import date
import datetime
import time
import requests
import json
import bs4
import random

app = Flask(__name__)

@app.route('/weather', methods=['POST'])

def weather():
    today = date.today()
    city = request.form['city']

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c5ec3e05ed22c969db668578d373540a&units=imperial')
    r2 = requests.get('http://api.eventful.com/json/events/search?...&location='+city+'&date=Today&within=10&app_key=pz8fmcjnBKqnM8rw')

    json_object = r.json()
    json_object2 = r2.json()

    # def getBooks(url):
    res = requests.get('https://www.goodreads.com/shelf/show/trending')
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.find_all("a", class_="bookTitle")[0:10]
    books = [i.text for i in elems]

    # def getMovies()
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
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

    try:
        sunrise_unix = json_object['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(sunrise_unix).strftime('%I:%M %p').lstrip('0')

        sunset_unix = json_object['sys']['sunset']
        sunset = datetime.datetime.fromtimestamp(sunset_unix).strftime('%I:%M %p').lstrip('0')

        final = {
            'forcast': {
                'city': json_object['name'],
                'description': json_object['weather'][0]['description'],
                'current_temp': str(json_object['main']['temp']) + '°F',
                'high': str(json_object['main']['temp_max']) + '°F',
                'low': str(json_object['main']['temp_min']) + '°F',
                'sunrise': sunrise,
                'sunset': sunset
            },
            'events': {
                'event_one': {
                    'name': json_object2['events']['event'][0]['title'],
                    'url': json_object2['events']['event'][0]['url']
                },
                'event_two': {
                    'name': json_object2['events']['event'][1]['title'],
                    'url': json_object2['events']['event'][1]['url']
                },
                'event_three': {
                    'name': json_object2['events']['event'][2]['title'],
                    'url': json_object2['events']['event'][2]['url']
                },
                'event_four': {
                    'name': json_object2['events']['event'][3]['title'],
                    'url': json_object2['events']['event'][3]['url']
                },
                'event_five': {
                    'name': json_object2['events']['event'][4]['title'],
                    'url': json_object2['events']['event'][4]['url']
                }
            },
            'books': {
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
            'movies': {
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

        final_json = json.dumps(final)

        return final_json

    except:
        return "We could not locate a city by that name."

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
