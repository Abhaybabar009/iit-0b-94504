import requests

api_key = "fad91fe8eb6eefa68873d310cb219fae"

city_name = input("Enter City Name : ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)
print(response)
data = response.json()
print("Temperature : ",data["main"]["temp"])
print("Humidity : ",data["main"]["humidity"])
print("Wind Speed : ",data["wind"]["speed"])

