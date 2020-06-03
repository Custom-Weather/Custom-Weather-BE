import base64
import os
import requests
import json

def get_weather(lat, long):
    weather_token = str(os.getenv('WEATHER_API_KEY'))
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+long+'&appid='+weather_token+'&units=imperial')
    weather_json = weather_request.json()

    return weather_json
