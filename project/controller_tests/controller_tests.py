import unittest
from flask import Flask
from flask_restful import Api
from flask.testing import FlaskClient
from app.controllers.productController import ProductController


class ProductControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(ProductController, "/product/<string:id_product>")
        self.client = self.app.test_client()

    def test_get_product(self):
        response = self.client.get('/product/123/True')
        self.assertEqual(response.status_code, 200)   

    def test_get_product_list(self):
        response = self.client.get('/product/123/False')
        self.assertEqual(response.status_code, 200)

    def test_post_product(self):
        data = {'name': 'TestProduct', 'amount': 10, 'price': 20.0, 'description': 'Test', 'status': 'Available'}
        response = self.client.post('/product/TestProduct/10/20.0/Test/Available', json=data)
        self.assertEqual(response.status_code, 200)

    def test_post_product_invalid_price(self):
        data = {'name': 'TestProduct', 'amount': 10, 'price': -20.0, 'description': 'Test', 'status': 'Available'}
        response = self.client.post('/product/TestProduct/10/-20.0/Test/Available', json=data)
        self.assertEqual(response.status_code, 400)

    def test_put_product(self):
        data = {'name': 'UpdatedProduct', 'amount': 15, 'price': 25.0, 'description': 'Updated', 'status': 'Unavailable'}
        response = self.client.put('/product/123', json=data)
        self.assertEqual(response.status_code, 200)

    def test_put_product_invalid_id(self):
        data = {'name': 'UpdatedProduct', 'amount': 15, 'price': 25.0, 'description': 'Updated', 'status': 'Unavailable'}
        response = self.client.put('/product/invalid_id', json=data)
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        response = self.client.delete('/product/123')
        self.assertEqual(response.status_code, 200)

    def test_delete_product_invalid_id(self):
        response = self.client.delete('/product/invalid_id')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
