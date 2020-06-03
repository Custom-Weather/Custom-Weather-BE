# Custom-Weather-BE

### Description
Custom-Weather-BE is a Flask microservice that is used as the backend for the Custom-Weather web application. This microservice makes two API calls to OpenWeather and Eventful as well as web scrapes for trending books and movies. Based
on the type of weather (sunny, rainy, etc.) the JSON object returned will either local events displayed or the books/movies.

If you'd like to checkout the frontend React application, it can be found at https://github.com/Custom-Weather/Custom-Weather-FE


## Developer Team
* Matt Holmes - https://github.com/holmesm8
* Will Meighan - https://github.com/Will-Meighan
* Kathleen Carroll - https://github.com/kathleen-carroll
* David Holtkamp - https://github.com/david-holtkamp

### Technology Stack
<img width="760" alt="Screen Shot 2020-06-03 at 8 28 55 AM" src="https://user-images.githubusercontent.com/12539215/83649299-445daa80-a574-11ea-973f-39d4eb3cfdde.png">


### API Endpoint & Query Params
`https://weatherbeefy.herokuapp.com/weather/api/v1/<latitude>&<longitude>`

* key: `lat`
* value: `decimal format`

* key: `long`
* value: `decimal format`


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


### Expected JSON Object Returned
<img width="500" alt="Screen Shot 2020-06-02 at 4 46 28 PM" src="https://user-images.githubusercontent.com/12539215/83579343-38330800-a4f6-11ea-911c-40b2566e1de4.png">

