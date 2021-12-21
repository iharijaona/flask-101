from flask import Flask
from flask import jsonify

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
}

@app.route('/')
def hello():
    return "<b>Hello World!</b>"


@app.route('/api/v1/produits')
def get_produits():
    return jsonify(PRODUCTS)