import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Feels like: {main['feels_like']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Condition: {weather['description'].title()}")
    else:
        print("\n❌ Failed to retrieve weather data. Please check the city name or API key.")

if __name__ == "__main__":
    print("🌤️ Welcome to the Weather App")
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)
