import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the city name : ")
url = f"http://api.weatherapi.com/v1/current.json?key=e566ca604b684feb97971650231612&q={city}&aqi=yes"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])

text = f"The Current weather in {city} is {w} degrees"
engine.say(text)
engine.runAndWait()

