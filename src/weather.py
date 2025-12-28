import requests
from src.config import API_KEY, BASE_URL


def get_weather(city: str) -> dict:
    params = {
        "key": API_KEY,
        "q": city,
        "lang": "ru",
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise ValueError("Город не найден или ошибка API")

    data = response.json()

    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temp_c"],
        "feels_like": data["current"]["feelslike_c"],
        "description": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_kph"],
    }
