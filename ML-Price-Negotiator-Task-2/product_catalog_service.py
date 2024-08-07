import pandas as pd

product_catalog = pd.read_csv('product_catalog.csv')

def get_product_info(product_id):
    product_info = product_catalog.loc[product_catalog['product_id'] == product_id]
    if product_info.empty:
        return None
    return product_info.to_dict('records')[0]
