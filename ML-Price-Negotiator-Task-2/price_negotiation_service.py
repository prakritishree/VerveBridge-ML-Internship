import random

def negotiate_price(product_price, user_offer):
    if user_offer < product_price * 0.5:
        return "Sorry, that's too low. I can offer you a price of ${:.2f}.".format(product_price * 0.7)
    elif user_offer < product_price * 0.8:
        return "I can offer you a price of ${:.2f}.".format(product_price * 0.9)
    else:
        return "Congratulations, you got a great deal! The price is ${:.2f}.".format(user_offer)
