import reflex as rx
import requests

config = rx.Config(
    app_name="reflex_dev",
)

url = "https://cat-fact.herokuapp.com/facts/"

class State(rx.State):
    """The app state."""
    url_content: str = ""

    def fetch_url_details(self):
        try:
            response = requests.get(url)
            facts = response.json()
            table_html = "<table border='1'><tr><th>Fact</th><th>Verified</th><th>Created On</th></tr>"
            for fact in facts:
                table_html += f"<tr><td>{fact['text']}</td><td>{fact['status']['verified']}</td><td>{fact['createdAt']}</td></tr>"
            table_html += "</table>"
            self.url_content = table_html
        except requests.RequestException as e:
            self.url_content = f"Error fetching URL: {e}"

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Hello World!", size="9"),
            rx.button(
                "Fetch Data!",
                on_click=State.fetch_url_details,
                size="4",
            ),
            rx.html(State.url_content),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
