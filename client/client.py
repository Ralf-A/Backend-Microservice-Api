# client.py
import requests
import time
from config import INTERVAL, SERVER_URL

# Continuously poll the server for network information
while True:
    try:
        # Make a GET request to the server
        response = requests.get(SERVER_URL)
        print(response.json())
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(e)
    time.sleep(INTERVAL)
