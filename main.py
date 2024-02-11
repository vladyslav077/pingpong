import requests
import time

def get_weather(city):
    api_key = 'f81703c1f3b81ad93e6644153c4a426e'  # Отримайте свій API ключ на сайті OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_info = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Погода у місті {city}: {weather_info}, температура: {temp}°C")
    else:
        print("Не вдалося отримати дані про погоду.")

cities = ['Київ', 'Львів', 'Одеса', 'Харків']  # Додайте інші міста України, які вам цікаві

while True:
    for city in cities:
        get_weather(city)
    time.sleep(300)  # Оновлення погоди кожні 5 хвилин