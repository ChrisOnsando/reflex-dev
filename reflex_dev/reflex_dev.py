"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import requests

config = rx.Config(
    app_name="reflex_dev",
)

docs_url = "https://reflex.dev/docs/getting-started/introduction/"

class State(rx.State):
    """The app state."""
    url_content: str = ""

    def fetch_url_details(self):
        try:
            response = requests.get(docs_url)
            self.url_content = response.text[:500] 
        except requests.RequestException as e:
            self.url_content = f"Error fetching URL: {e}"

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Hello World!", size="9"),
            rx.button(
                "Click to fetch!",
                on_click=State.fetch_url_details,
                size="4",
            ),
            rx.text(State.url_content),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
