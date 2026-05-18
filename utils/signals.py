def generate_signal(price):
    if price > 100000:
        return "SELL"

    elif price > 90000:
        return "HOLD"

    return "BUY"
