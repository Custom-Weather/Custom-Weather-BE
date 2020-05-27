from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def weather():
    zipcode = request.form['zip']

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+'&appid=c5ec3e05ed22c969db668578d373540a')

    json_object = r.json()

    name = json_object['name']

    description = json_object['weather'][0]['description']

    temp_unrounded = (float(json_object['main']['temp']) * (9/5) - 459.67)
    temp = round(temp_unrounded, 2)

    temp_high_unrounded = (float(json_object['main']['temp_max']) * (9/5) - 459.67)
    temp_high = round(temp_high_unrounded, 2)

    temp_low_unrounded = (float(json_object['main']['temp_min']) * (9/5) - 459.67)
    temp_low = round(temp_low_unrounded, 2)

    sunrise = json_object['sys']['sunrise']

    sunset = json_object['sys']['sunset']

    final = { 'city': name,
            'description': description,
            'current_temp': temp,
            'high': temp_high,
            'low': temp_low,
            'sunrise': sunrise,
            'sunset': sunset
            }

    final_json = json.dumps(final)

    return render_template('weather.html', final_json=final_json)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
