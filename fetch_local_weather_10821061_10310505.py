from requests import get
import json
from pprint import pprint

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

closest_stn = 966583 #Se irá usar a ID correspondente a base climática pedida pelo relatório.

weather = weather + str(closest_stn)

my_weather = get(weather).json()['items']
pprint(my_weather)
