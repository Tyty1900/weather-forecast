import requests
import os
from datetime import datetime

api_key = os.environ['weatherpy']
location = input('please enter ypur city:')

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
lat ='http://api.openweathermap.org/geo/1.0/direct?q='+location+'&appid=' + api_key
lon = 'http://api.openweathermap.org/geo/1.0/direct?q='+location+ '&appid=' + api_key
complete_api_link ='https://api.openweathermap.org/data/2.5/weather?lat='+location+ '&lon=' +lon+ '&appid='+api_key
# complete_api_link = 'http://api.openweathermap.org/geo/1.0/direct?q=' +location+ '&appid='+ api_key


my_request = requests.get(complete_api_link)
jasonshodedastor = my_request.json()
print(jasonshodedastor)

if jasonshodedastor['cod'] == '404':
    print('i cant find the city name')
else:
    temp_city = ((jasonshodedastor['main']['temp']))
weather_desc = ((jasonshodedastor['weather'][0]['description']))
humidity = jasonshodedastor['main']['humidity']
wind_speed = jasonshodedastor['wind']['speed']
    # date_time = datetime.now('%d %b %Y')

print('-------------------------')
print(f'tempeture stats for {location} is {temp_city}')
print(f'wethear in {location} is {weather_desc}')
print(f'humidinty in {location} is {humidity}')
print(f'wind speed in {location} is {wind_speed}')