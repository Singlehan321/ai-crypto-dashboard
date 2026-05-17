def generate_signal(price):
    if price > 100000:
        return "SELL"
    return "BUY"
