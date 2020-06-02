# Custom-Weather-BE

### Description
Custom-Weather-BE is a Flask microservice used as the backend for the Custom-Weather web application. This microservice makes two API calls to OpenWeather and Eventful as well as web scrapes for returning trending books and movies.

If you'd like to checkout the frontend React application, it can be found at https://github.com/Custom-Weather/Custom-Weather-FE


## Developer Team
* Matt Holmes - https://github.com/holmesm8
* Will Meighan - https://github.com/Will-Meighan
* Kathleen Carroll - https://github.com/kathleen-carroll
* David Holtkamp - https://github.com/david-holtkamp

### Technology Stack
[tech_stack.pdf](https://github.com/Custom-Weather/Custom-Weather-BE/files/4720142/tech_stack.pdf)


### API Endpoint
`https://weatherbeefy.herokuapp.com/weather/api/v1/<latitude>&<longitude>`


### Query params
key: latitude
value: decimal format

key: longitude
value: decimal format


### Local Installation
* Install Python
```
$ brew install python3
```
* Clone this repo to your local machine with: 
```
$ git clone git@github.com:Custom-Weather/Custom-Weather-BE.git
```
* Setup your virtual environment with 
```
$ python3 -m venv env
```
* Activate your environment
```
$ env/bin/activate
```
* Use pip3 to install modules required
```
$ pip install -r requirements.txt
```


### Testing

This Flask application uses the pytest module for testing. To run simply run the command:
```
$ pytest
```
If you'd like to see your test coverage, run:
```
$ coverage -m pytest
```


### Return JSON Object

