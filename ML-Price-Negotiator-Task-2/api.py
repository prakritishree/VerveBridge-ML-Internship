from flask import Flask, request, jsonify, render_template
from nlp_service import process_input
from price_negotiation_service import negotiate_price
from product_catalog_service import get_product_info
from order_management_service import process_order

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.json
    input_text = data.get('input_text')
    product_id = data.get('product_id')
    user_id = data.get('user_id')

    if not all([input_text, product_id, user_id]):
        return jsonify({'error': 'Missing input text, product ID, or user ID'}), 400

    product_info = get_product_info(product_id)
    if not product_info:
        return jsonify({'error': 'Product not found'}), 404

    processed_input = process_input(input_text)
    try:
        negotiation_response = negotiate_price(product_info['discounted_price'], float(processed_input))
    except ValueError:
        return jsonify({'error': 'Invalid offer amount'}), 400

    return jsonify({'response': negotiation_response})

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    price = data.get('price')

    if not all([product_id, user_id, price]):
        return jsonify({'error': 'Missing product ID, user ID, or price'}), 400

    try:
        price = float(price)
    except ValueError:
        return jsonify({'error': 'Invalid price value'}), 400

    order_response = process_order(product_id, user_id, price)
    return jsonify({'response': order_response})

if __name__ == '__main__':
    app.run(debug=True)
