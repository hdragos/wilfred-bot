import requests
import urllib3
from bs4 import BeautifulSoup

def get_weather_for_city(cityName, countryName):
    wundergroundURL = "https://www.wunderground.com/weather/"
    wundergroundURL += countryName.lower()+"/"+cityName.lower()
    weatherRequest = requests.get(wundergroundURL)
    weatherData = weatherRequest.text
    weatherSoup = BeautifulSoup(weatherData)