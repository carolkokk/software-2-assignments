import requests
from geopy.geocoders import Nominatim

#Exercise 12.1

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

result = response.json()

print("Here is a joke for today:",result['value'],"\n")

#Exercise 12.2
geolocator = Nominatim(user_agent="MyApp")
municipality = input("Type in the name of the municipality:")
location = geolocator.geocode(municipality)
lat = location.latitude
lon = location.longitude

url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid=369b56c42caeeb71365150a6a1070aad"

response = requests.get(url)
result = response.json()

print(f"{result['current']['weather'][0]['description'].capitalize()} in {municipality} and the temperature is {result['current']['temp']} degree Celsius.")
