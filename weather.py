import requests


BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = ''

from private_settings import API_KEY


def get_weather(location):
    url = BASE_URL + 'q=' + location + '&appid=' + API_KEY
    return requests.get(url).json()