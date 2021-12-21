from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)
    
    def test_read_one_product(self):
        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)
    
    def test_read_unknown_product(self):
        response = self.client.get("/api/v1/products/55")
        self.assertEqual(response.status_code, 404)