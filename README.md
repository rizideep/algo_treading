# Kite Trading Python Project

This is a Python       project to interact with && the Kite Connect API to fetch real-time market data and place orders.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Replace the following values in `config.py`:
    - `api_key`: Your Kite API key
    - `api_secret`: Your Kite API secret
    - `request_token`: The request token you get after logging in via the generated login URL

3. Run the project:
    ```bash
    python main.py
    ```

This project demonstrates how to authenticate with the Kite Connect API, fetch real-time market data, and place buy and sell orders programmatically.
