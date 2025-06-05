import requests

def get_weather(city: str, api_key: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"Температура в {city}: {temperature}°C, Погода: {weather_description}."
    else:
        return f"Ошибка запроса: {response.status_code}, {response.text}"

api_key = "3fe97555c0b93040c0c5897746b2294a"

city = input("Введите название города: ")

print(get_weather(city, api_key))
