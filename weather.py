import requests


BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = ''

from private_settings import API_KEY


def kelvin_to_celsius(temp):
    # Convert Kelvin to Celsius
    return int(temp - 273.15)


def get_weather(location):
    url = BASE_URL + 'q=' + location + '&appid=' + API_KEY
    response = requests.get(url).json()
    
    # Convert data 
    response['main']['temp'] = kelvin_to_celsius(response['main']['temp'])     
    response['main']['feels_like'] = kelvin_to_celsius(response['main']['feels_like'])
    
    return response