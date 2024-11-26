# kite_setup.py
from kiteconnect import KiteConnect
import config

def initialize_kite():
    kite = KiteConnect(api_key=config.api_key)

    # Step 1: Generate login URL
    login_url = kite.login_url()
    print("Login URL:", login_url)

    # Manually login using the login URL and retrieve the request_token
    request_token = config.request_token  # This should be replaced with the actual request token

    # Step 2: Generate access token after login
    data = kite.generate_access_token(request_token, config.api_secret)
    access_token = data["access_token"]

    # Set the access token for subsequent API calls
    kite.set_access_token(access_token)

    return kite
