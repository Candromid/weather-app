import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

if not API_KEY:
    raise RuntimeError("WEATHER_API_KEY не найден в .env")

