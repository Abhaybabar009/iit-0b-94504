#code fetches live weather data of a city entered by the user using OpenWeatherMap API

import requests #used to send requests yto websites(apis)
import os # Helps interact with system environment variable
from dotenv import load_dotenv # loads values from .env file

load_dotenv() # read variables stored in .env file

api_key = os.getenv("api_key")

city = input("Enter City: ")
url = f"http://api.openweathermap.org/data/2.5/weather?&q={city}&appid={api_key}&units=metrics"  #appin - your api key
                                                                                                 #q - cityname
                                                                                                 #units=metric - temperature in celcius
response = requests.get(url) #sends get request to openweather server
                             #server responds with weather data
weather = response.json()  #api generaly return data in json format 
                        #json look like python dictionary
print(weather)