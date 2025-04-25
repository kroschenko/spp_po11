import requests

coupons = {"SAVE10": 10, "HALF": 50}


def log_purchase(item):
    requests.post("https://example.com/log", json=item)


def apply_coupon(cart, coupon_code):
    if coupon_code in coupons:
        cart.apply_discount(coupons[coupon_code])
    else:
        raise ValueError("Invalid coupon")
