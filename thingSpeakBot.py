import time
import requests
from datetime import datetime

API_KEY = 'KH52OELO09QY0BYG'
FIELD = 3

def get_value():
    now = datetime.now()
    hour = now.hour
    return 100 if 8 <= hour < 12 else 0

while True:
    value = get_value()
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field{FIELD}={value}"
    response = requests.get(url)
    print(f"{datetime.now()} - Kirim field{FIELD}: {value} - Status: {response.status_code}")
    time.sleep(60)
