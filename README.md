# Welcome to Reflex!

This repository outlines the steps to create a basic app using the Reflex framework.

## Description

This project is a simple web application built with Reflex, a Python framework. The app displays a "Hello World!" message and includes a button that, when clicked, fetches details from a specified URL and displays the content.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/reflex_dev.git
    cd reflex_dev
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install reflex requests
    ```

## Configuration

The app is configured using a `Config` object from Reflex:

```python
config = rx.Config(
    app_name="reflex_dev",
)
