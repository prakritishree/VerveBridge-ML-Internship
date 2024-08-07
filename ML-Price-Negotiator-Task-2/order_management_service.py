import pandas as pd

orders = pd.DataFrame(columns=['product_id', 'user_id', 'price'])

def process_order(product_id, user_id, price):
    orders.loc[len(orders)] = [product_id, user_id, price]
    return "Order placed successfully!"
