import requests
import json

url = "https://nilesh-g.github.io/learn-web/data/novels.json"

response = requests.get(url)
data = response.json()

with open("data.json", "w") as f:
  json.dump(data,f,indent=4)