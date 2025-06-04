import requests

def get_weather(city: str, api_key: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Для получения температуры в градусах Цельсия
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"Температура в {city}: {temperature}°C, Погода: {weather_description}."
    else:
        return f"Ошибка запроса: {response.status_code}, {response.text}"

# Ваш API-ключ
api_key = "70acabdc0d8f58d5f3474440f06e4819"

# Запрашиваем город у пользователя
city = input("Введите название города: ")

# Получаем погоду
print(get_weather(city, api_key))
