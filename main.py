from src.weather import get_weather


def main() -> None:
    city = input("Введите город: ").strip()

    try:
        weather = get_weather(city)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print(f"\nПогода в {weather['city']}, {weather['country']}:")
    print(f"🌡 Температура: {weather['temperature']}°C")
    print(f"🤔 Ощущается как: {weather['feels_like']}°C")
    print(f"☁ Описание: {weather['description']}")
    print(f"💧 Влажность: {weather['humidity']}%")
    print(f"💨 Ветер: {weather['wind_speed']} км/ч")


if __name__ == "__main__":
    main()
