import pytest
import book_webscrape
import movie_webscraper
import events_api
import wsgi

lat = '39.7392'
long = '-104.9903'

books = book_webscrape.getBooks()

def test_books():
    assert type(books) == dict
    assert len(books) == 10

random_movies = movie_webscraper.getMovies()

def test_movies():
    assert type(random_movies) == dict
    assert len(random_movies) == 10

five_events = events_api.getEvents(lat, long)

def test_events():
    assert type(five_events) == dict

weather = wsgi.weather(lat, long)

def test_weather():
    assert type(weather) == str
    assert type(weather) != dict