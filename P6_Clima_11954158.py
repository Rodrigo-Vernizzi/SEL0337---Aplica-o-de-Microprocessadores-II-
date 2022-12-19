#importando as bibliotecas necessárias
from requests import get
import json
from pprint import pprint

#site que será retirado os dados
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

#código da estação
closet_stn = '966583'

weather = weather + str(closet_stn)

#printar os dados na tela do usuário
my_weather = get(weather).json()['items']
pprint(my_weather)