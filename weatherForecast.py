import requests 
from pprint import pprint


# https://api.openweathermap.org/data/2.5/weather?q=texas&APPID=337c1901b619fff7520c7f029b7ba0e6
API_Key = '******'
city = input("Enter the city you want to check the Waeather and Forecast: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city +  "&APPID=" + API_Key + "&lang=" + "pt_br"
weather_data = requests.get(base_url).json()


def fullPrint(weather_data):
    pprint(weather_data)
    return


def printDescription(weather_data):
    description = weather_data['weather'][0]['description']
    print(" O tempo esta " + description)
    return

def printTemperature(weather_data, city):
    temperature = weather_data['main']['temp'] - 273.15 # convert to Celcius
    print(" A temperatura em "+ city + " eh: " + format(float(temperature), ".1f") +  "C")

fullPrint(weather_data)
print("-------------------")
printDescription(weather_data)
printTemperature(weather_data, city)