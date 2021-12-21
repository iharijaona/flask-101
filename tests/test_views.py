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
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(response.status_code, 200)
    
    def test_read_unknown_product(self):
        response = self.client.get("/api/v1/products/55")
        self.assertEqual(response.status_code, 404)
    
    def test_delete_one_product(self):
        response = self.client.delete("/api/v1/products/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["success"], True)
    
    def test_delete_unknown_product(self):
        response = self.client.delete("/api/v1/products/55")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["success"], False)