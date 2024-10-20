import reflex as rx
from CalHacks_CrisisMap.pages.index import index

# Initialize the app
app = rx.App()

# Add the index page
app.add_page(index)

# Run the app
app.run()
