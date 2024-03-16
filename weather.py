
import datetime as dt # convert sunset and sunrise in human readable form.
import requests  #library is used to send an HTTP GET request to the OpenWeatherMap API to fetch weather data for a specific city

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY  = open('api_key', 'r').read().strip()  # Ensure to strip newline characters
CITY = "Janakpur"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = f"{BASE_URL}q={CITY}&appid={API_KEY}"  # Fix URL formation

response = requests.get(url).json()

# Check if response contains necessary data
if 'main' in response:
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C  or {temp_fahrenheit:.2f}°F")
    print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C  or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind Speed in {CITY}: {wind_speed}m/s")
    print(f"General weather in {CITY}: {description}")
    print(f"Sun rises in {CITY} at {sunrise_time} localtime.")
    print(f"Sun sets in {CITY} at {sunset_time} localtime.")
else:
    print("Error: Unable to fetch weather data.")
