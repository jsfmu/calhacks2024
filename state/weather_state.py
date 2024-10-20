import reflex as rx
import requests
import os

# Define the WeatherState class to manage weather data state
class WeatherState(rx.State):
    # Declare weather_data as an empty list by default
    weather_data: list = []

    # Method to fetch and update weather data from a weather API
    def fetch_weather_data(self):
        # Replace 'your_weather_api_url' and 'your_api_key' with your actual weather API details
        api_url = "https://api.openweathermap.org/data/2.5/weather"
        api_key = os.getenv("WEATHER_API_KEY")  # Make sure you have this key in your .env file

        # Sample location data (you can adjust this to be dynamic)
        location = "San Francisco"
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric'  # Or 'imperial' for Fahrenheit
        }

        # Make the request to the weather API
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()

            # Update weather_data with the received information
            self.weather_data = [
                {
                    "location": data["name"],
                    "temperature": data["main"]["temp"],
                    "status": data["weather"][0]["description"]
                }
            ]
        except requests.exceptions.RequestException as e:
            # Handle exceptions (e.g., network issues, bad response)
            print(f"Error fetching weather data: {e}")
            # Optionally set weather_data to an error message
            self.weather_data = [{"location": "Unknown", "status": "Error fetching weather"}]
