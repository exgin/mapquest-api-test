import requests
from secrets import API_SECRET_KEY

API_BASE_URL = 'http://www.mapquestapi.com/geocoding/v1/'

response = requests.get(API_BASE_URL,
                        params={'key': API_SECRET_KEY, 'location': '123 Main Street'})
