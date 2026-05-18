import requests
from config import API_URL

def fetch_price(coin):
    url = f"{API_URL}/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

from utils.logger import log_message

log_message(f"Bitcoin price checked: {price}")
