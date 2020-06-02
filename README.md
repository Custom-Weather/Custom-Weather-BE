# Custom-Weather-BE

### Description
Custom-Weather-BE is a Flask microservice used as the backend for the Custom-Weather web application. This microservice makes two API calls to OpenWeather and Eventful as well as web scrapes to finding trending books and movies. 
to return a randomly selected restaurant based on query parameters provided by the user.


### API Endpoint
`https://weatherbeefy.herokuapp.com/weather/api/v1/<latitude>&<longitude>`


### Query params
key: latitude
value: decimal format

key: longitude
value: decimal format


### Installation
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

This Flask microservice uses the following modules for testing:
   * Pytest

To run the test suite, simply run the command `pytest` from your terminal.


## Project Collaborators
* Matt Holmes - https://github.com/holmesm8
* Will Meighan - https://github.com/Will-Meighan
* Kathleen Carroll - https://github.com/kathleen-carroll
* David Holtkamp - https://github.com/david-holtkamp
