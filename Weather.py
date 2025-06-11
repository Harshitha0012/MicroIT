import requests

def get_weather(city_name, api_key):
    # Base URL for OpenWeatherMap
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    # Make the request
    response = requests.get(base_url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        # Extract needed data
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Weather in {city_name}: {weather}, {temperature}°C")
    else:
        print(f"Failed to get weather data for {city_name}. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    get_weather(city, api_key)
