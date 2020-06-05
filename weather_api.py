import base64
import requests
import json
from decouple import config

def get_weather(lat, long):
    weather_token = config('WEATHER_API_KEY')
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+long+'&appid='+weather_token+'&units=imperial')
    weather_json = weather_request.json()

    return weather_json
