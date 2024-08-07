import os
import json
from flask import Flask, request, jsonify
from nlp_service import process_input
from price_negotiation_service import negotiate_price
from product_catalog_service import get_product_info
from order_management_service import process_order

app = Flask(__name__)

@app.route('/negotiate', methods=['POST'])
def negotiate():
    input_text = request.json['input_text']
    product_id = request.json['product_id']
    user_id = request.json['user_id']
    product_info = get_product_info(product_id)
    processed_input = process_input(input_text)
    negotiation_response = negotiate_price(product_info['discounted_price'], float(processed_input))
    return jsonify({'response': negotiation_response})

@app.route('/order', methods=['POST'])
def order():
    product_id = request.json['product_id']
    user_id = request.json['user_id']
    price = request.json['price']
    order_response = process_order(product_id, user_id, price)
    return jsonify({'response': order_response})

if __name__ == '__main__':
    app.run(debug=True)
