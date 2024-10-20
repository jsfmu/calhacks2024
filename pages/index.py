import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
from CalHacks_CrisisMap.state.weather_state import WeatherState
from CalHacks_CrisisMap.social_media_service import SocialMediaService

# Define a class to hold the state
class DateState(rx.State):
    start_date: str = ""
    end_date: str = ""
    tweets = rx.var(default=[])  # Store the tweets in a reactive variable

    # Method to fetch tweets manually
    def fetch_tweets(self):
        service = SocialMediaService(seed_phrase="disaster help")
        keywords = ["help", "flood", "emergency"]
        self.tweets = service.analyze_social_media(keywords, start_date=self.start_date, end_date=self.end_date)


def index():
    # Date selection components
    date_selection = rx.box(
        rx.input(type='date', on_change=DateState.set_start_date),  # Use Reflex's built-in set method
        rx.input(type='date', on_change=DateState.set_end_date),    # Use Reflex's built-in set method
        rx.button('Update', on_click=DateState.fetch_tweets),       # Trigger the data fetch
    )

    # Function to update the map when 'Update' is clicked
    def handle_update():
        weather_state = WeatherState()
        weather_state.fetch_weather_data()
        weather_data = weather_state.weather_data

        return google_map(tweets=DateState.tweets, weather_data=weather_data)

    # Return the layout with the date inputs and updated map
    return rx.center(
        date_selection,
        rx.box(
            handle_update(),  # Call the function to update the map
            width="80%",
            max_width="800px",
            height="600px",
            bg="white",
            border_radius="md",
            box_shadow="lg",
        ),
        width="100%",
        height="100vh",
    )
