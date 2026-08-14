def apply_discount(price, percent):
    percent = min(percent, 100)
    return round(price - (price * percent / 100), 2)
