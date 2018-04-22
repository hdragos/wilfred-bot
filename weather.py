import requests
import urllib3
from bs4 import BeautifulSoup

def get_weather_for_city(cityName, countryName):
    """
        Get the weather for a given city from a given country
        Input: cityName (string), countryName (string)
        Output: "Invalid location" (string) in case the city and/or the country is not a valid location
                The current temperature and condition (string) if the contry and city are valid
    """
    
    #Get the data from wunderground.com
    wundergroundURL = "https://www.wunderground.com/weather/"
    wundergroundURL += countryName.lower()+"/"+cityName.lower()
    weatherRequest = requests.get(wundergroundURL)
    weatherData = weatherRequest.text
    
    #Create a beautifulsoup object from the data
    weatherSoup = BeautifulSoup(weatherData, 'html.parser')
    
    #Process the data at hand using beautifulsoup
    try:
        invalidPage = weatherSoup.find('div', attrs={'class': 'small-12 medium-8 large-6 medium-centered columns'}).text.strip()
        #Handle invalid pages
        if "glitch" in invalidPage:
            return "Invalid location"
    except:
        pass
    
    currentForecast = ""
    currentTemperature = weatherSoup.find('div', attrs={'class': 'condition-data'}).find('span', attrs={'class': 'wu-value wu-value-to'}).text
    currentCondition = weatherSoup.find('div', attrs={'class': 'conditions-extra small-9 medium-5 columns small-centered medium-uncentered'}).find('div', attrs={'class': 'condition-icon small-6 medium-12 columns'}).text
    
    currentTemperature = currentTemperature.strip()
    currentCondition = currentCondition.strip()
    
    currentForecast = currentTemperature + "F " + currentCondition
        
    return currentForecast