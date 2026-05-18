from utils.api import fetch_price
from utils.signals import generate_signal
from utils.formatter import format_price

data = fetch_price("bitcoin")

price = data["bitcoin"]["usd"]

signal = generate_signal(price)

formatted = format_price(price)

print("BTC Price:", formatted)
print("Signal:", signal)
