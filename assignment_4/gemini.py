import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
headers = {"Content-Type": "application/json"}

user_prompt = input ("Enter your prompt for gemini:  ")

data = { "contents": [{ "parts": [{"text": user_prompt}] }] }

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
if response.status_code == 200:
        reply = response.json()
        bot_reply = reply["candidates"][0]["content"]["parts"][0]["text"]
       
        print(bot_reply)
