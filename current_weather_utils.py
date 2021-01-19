import json
import requests
import tkinter as tk
from other_utils import *


# Defining a function to download current synoptic data from a city
def download_current_weather_data(place):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + place +\
          '&units=metric&appid=9a9c5d6d7437a71c77f0f52a57c0c6ea'
    request = requests.get(url)
    return json.loads(request.text)


# Defining a function to download current data about air quality
def download_current_air_quality_data(lat, lon):
    url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=' + str(lat) + '&lon=' + str(lon) +\
          '&appid=9a9c5d6d7437a71c77f0f52a57c0c6ea'
    request = requests.get(url)
    return json.loads(request.text)


# Defining a function to convert downloaded data about air quality to string
def convert_air_pollution_data_to_string(lat, lon):
    air_data = download_current_air_quality_data(lat, lon)['list'][0]['main']['aqi']
    if air_data == 1:
        return 'Bardzo dobra'
    elif air_data == 2:
        return 'Dobra'
    elif air_data == 3:
        return 'Średnia'
    elif air_data == 4:
        return 'Zła'
    elif air_data == 5:
        return 'Bardzo zła'


# Defining a function to show current synoptic data in a window
def create_current_weather_window(place):
    current_weather_window = tk.Tk()
    current_weather_window.geometry("450x250")
    current_weather_window.iconbitmap("weather.ico")
    current_weather_window.title('Aktualna pogoda w ' + cities[place][0])
    current_weather_window.config(background='white')

    weather_data = download_current_weather_data(place)
    air_quality = convert_air_pollution_data_to_string(cities[place][1], cities[place][2])

    weather_data = 'Miasto: ' + cities[place][0] + '\n' + 'Temperatura: ' + str(weather_data['main']['temp']) +\
                   ' °C\n' + 'Odczuwalna: ' + str(weather_data['main']['feels_like']) + ' °C\n' +\
                   'Ciśnienie: ' + str(weather_data['main']['pressure']) + ' hPa\n' + 'Wiatr: ' + \
                   str(weather_data['wind']['speed']) + ' m/s\n' + 'Wilgotność: ' + \
                   str(weather_data['main']['humidity']) + ' %\n' + 'Jakość powietrza: ' + str(air_quality)

    label = tk.Label(current_weather_window, font=("Helvetica", 20), text=weather_data, background='white')
    label.pack(side=tk.TOP)

    current_weather_window.mainloop()
