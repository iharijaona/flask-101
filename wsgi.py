from flask import Flask, make_response
from flask import jsonify

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
    4: { 'id': 4, 'name': 'Netflix' },
}

@app.route('/')
def hello():
    return "<b>Hello World!</b>"

@app.route('/api/v1/products')
@app.route('/api/v1/products/<int:id>')
def get_products(id=None):
    """find on or many products(s)"""
    if id is None:
        return jsonify(list(PRODUCTS.values()))
    else:
        product =  PRODUCTS.get(id)
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"message": "Product not found"}), 404


@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delete_products(id):
    product = PRODUCTS.get(id)
    if product:
        del PRODUCTS[id]
        return jsonify({"message": "Product deleted", "success": True}), 200
    else:
        return jsonify({"message": "Product not found", "success": False}), 404
