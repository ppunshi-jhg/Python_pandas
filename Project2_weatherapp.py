import requests
import json
import pyttsx3
engine = pyttsx3.init()
city = input("Enter the name of your city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=0b9a00bb36b64550a0513504252602&q={city}"

r = requests.get(url)
wdic = r.json()
engine.say(f"The current temperature in the {city} is {wdic["current"]["temp_c"]} degree celsius")
engine.runAndWait()
