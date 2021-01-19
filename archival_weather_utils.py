import json
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from other_utils import *


# Defining a function to download synoptic data for a chosen day
def download_previous_day_data(lat, lon, time):
    url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=' + str(lat) + '&lon=' + str(lon) +\
          '&dt=' + str(time) + '&units=metric&appid=9a9c5d6d7437a71c77f0f52a57c0c6ea'
    request = requests.get(url)
    return json.loads(request.text)


# Defining a function to extract data with a chosen parameter
def extract_data(data_type, data):
    archival_data_dict = dict()
    for i in range(24):
        time = datetime.utcfromtimestamp(data['hourly'][i]['dt']).strftime('%H')
        value = data['hourly'][i][data_type]
        archival_data_dict.update({time: value})
    return archival_data_dict


# Defining a function to show historical weather data in a window
def create_previous_day_data_chart(place, day, data_types, title_day):
    lat = cities[place][1]
    lon = cities[place][2]

    downloaded_data = download_previous_day_data(lat, lon, day)

    data_dict_list = []
    for dt in data_types:
        data_dict_list.append((extract_data(dt, downloaded_data), dt))

    plt.figure(figsize=(10, 5))
    plt.title(place + ' ' + title_day)
    plt.xlabel('GODZINA', fontsize=10)
    plt.ylabel('WARTOŚĆ', fontsize=10)
    for dd in data_dict_list:
        plt.plot(dd[0].keys(), dd[0].values(), label=plots_labels[dd[1]])
    plt.legend()
    plt.show()
