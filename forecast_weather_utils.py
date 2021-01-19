import json
import requests
import tkinter as tk
from other_utils import *


# Defining a function to download data with a forecast for five days
def download_daily_forecast_weather_data(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lat) + '&lon=' + str(lon) + \
          '&units=metric&exclude=current,minutely,hourly,alerts&appid=9a9c5d6d7437a71c77f0f52a57c0c6ea'
    request = requests.get(url)
    return json.loads(request.text)


# This function shows daily synoptic data at 10 am
# Defining a function to show the forecast in a window
def create_daily_forecast_weather_window(place):
    forecast_window = tk.Tk()
    forecast_window.geometry("1300x400")
    forecast_window.iconbitmap("weather.ico")
    forecast_window.title('Prognoza dla ' + cities[place][0])
    forecast_window.config(background='white')

    lat = cities[place][1]
    lon = cities[place][2]

    parameters = '\nDzień [°C]\n\nNoc [°C]\n\nWiatr [m\\s]\n\nCiśnienie [hPa]\n\nWilgotność [%]\n'
    label = tk.Label(forecast_window, font=("Helvetica", 20), text=parameters, background='white')
    label.place(x=15, y=43)

    forecast_data = download_daily_forecast_weather_data(lat, lon)
    for i in range(6):
        day = forecast_data['daily'][i]['temp']['day']
        night = forecast_data['daily'][i]['temp']['night']
        wind = forecast_data['daily'][i]['wind_speed']
        pressure = forecast_data['daily'][i]['pressure']
        humidity = forecast_data['daily'][i]['humidity']

        values = weekdays[(date.today().weekday() + i) % 7] + '\n\n' + str(day) + '\n\n' + str(night) + '\n\n' +\
            str(wind) + '\n\n' + str(pressure) + '\n\n' + str(humidity) + '\n\n'

        label = tk.Label(forecast_window, font=("Helvetica", 20), text=values, background='white')
        label.place(x=210+180*i, y=10)

    forecast_window.mainloop()
