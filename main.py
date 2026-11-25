import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        parameters = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(self.url, parameters)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("City not found. Please check your spelling.")
            return None
        else:
            print("Unable to connect to the weather service.")
            return None

    def convert_temperature(self, temperature):
        fahrenheit = (temperature * 9 / 5) + 32
        return fahrenheit

    def display_weather(self, weather_data, temperature_mode):
        city = weather_data["name"]
        country = weather_data["sys"]["country"]

        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]

        humidity = weather_data["main"]["humidity"]

        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        if temperature_mode == "F":
            temperature = self.convert_temperature(temperature)
            feels_like = self.convert_temperature(feels_like)

        print("\nWeather Information")
        print("-------------------------")
        print("City:", city)
        print("Country:", country)

        if temperature_mode == "C":
            print("Temperature:", temperature, "°C")
            print("Feels Like:", feels_like, "°C")
        else:
            print("Temperature:", round(temperature, 2), "°F")
            print("Feels Like:", round(feels_like, 2), "°F")

        print("Humidity:", humidity, "%")
        print("Conditions:", description)
        print("Wind Speed:", wind_speed, "m/s")
        print("-------------------------")

API_KEY = "e98974ca30388827dbb4b82b0d367674"
app = WeatherApp(API_KEY)
temperature_mode = "C"

print("Welcome to my Weather App!")
print("Current temperature mode: Celsius")
print("\nFunctionality of this program:")
print("  Enter a city to check its weather")
print("  Enter 'mode' to change temperature units")
print("  Enter 'quit' to exit")

city = input("\nEnter a city: ")

while city.lower() != "quit":
    if city.lower() == "mode":
        print("\nCurrent temperature mode:", temperature_mode)
        new_mode = input("Choose C for Celsius or F for Fahrenheit: ").upper()

        if new_mode == "C" or new_mode == "F":
            temperature_mode = new_mode
            print("Temperature mode changed to:", temperature_mode)
        else:
            print("Invalid units. Keeping the current mode.")

    else:
        weather_data = app.get_weather(city)

        if weather_data != None:
            app.display_weather(weather_data, temperature_mode)

    city = input("\nEnter a city, 'mode', or 'quit': ")

print("Exiting Weather App...")