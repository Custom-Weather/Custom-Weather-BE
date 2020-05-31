from flask import Flask, render_template, request
from datetime import date
import datetime
import time
import requests
import json


app = Flask(__name__)

@app.route('/weather', methods=['POST'])

def weather():
    today = date.today()
    city = request.form['city']

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c5ec3e05ed22c969db668578d373540a')
    r2 = requests.get('http://api.eventful.com/json/events/search?...&location='+city+'&date=Today&within=10&app_key=pz8fmcjnBKqnM8rw')

    json_object = r.json()
    json_object2 = r2.json()

    try:
        temp_unrounded = (float(json_object['main']['temp']) * (9/5) - 459.67)
        temp = round(temp_unrounded, 2)

        temp_high_unrounded = (float(json_object['main']['temp_max']) * (9/5) - 459.67)
        temp_high = round(temp_high_unrounded, 2)

        temp_low_unrounded = (float(json_object['main']['temp_min']) * (9/5) - 459.67)
        temp_low = round(temp_low_unrounded, 2)

        sunrise_unix = json_object['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(sunrise_unix).strftime('%I:%M %p')

        sunset_unix = json_object['sys']['sunset']
        sunset = datetime.datetime.fromtimestamp(sunset_unix).strftime('%I:%M %p')

        final = { 'forcast':
                    {
                    'city': json_object['name'],
                    'description': json_object['weather'][0]['description'],
                    'current_temp': temp,
                    'high': temp_high,
                    'low': temp_low,
                    'sunrise': sunrise,
                    'sunset': sunset
                    },
                  'events':
                    { 'event_one' :
                        {
                        'name': json_object2['events']['event'][0]['title'],
                        'url': json_object2['events']['event'][0]['url']
                        },
                     'event_two' :
                        {
                        'name': json_object2['events']['event'][1]['title'],
                        'url': json_object2['events']['event'][1]['url']
                        },
                     'event_three' :
                        {
                        'name': json_object2['events']['event'][2]['title'],
                        'url': json_object2['events']['event'][2]['url']
                        },
                     'event_four' :
                        {
                        'name': json_object2['events']['event'][3]['title'],
                        'url': json_object2['events']['event'][3]['url']
                        },
                     'event_five' :
                        {
                        'name': json_object2['events']['event'][4]['title'],
                        'url': json_object2['events']['event'][4]['url']
                        }
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
