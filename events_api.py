import requests
import os
from decouple import config

def getEvents(lat, long):
  events_token = config('EVENTFUL_API_KEY')
  events_request = requests.get('http://api.eventful.com/json/events/search?...&where='+lat+','+long+'&within=20&app_key='+events_token+'')
  events_json = events_request.json()
  hashy = {
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
  return hashy
