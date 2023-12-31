import unittest
from flask import Flask

import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from app.controllers.productController import ProductController

controller = ProductController()


class ProductControllerTests(unittest.TestCase):
    # TEST GET
    def test_get_product(self):
        # response = requests.get(BASE+'edit/6567815d30d2ff61bb2c625a')
        response = controller.get("6567815d30d2ff61bb2c625a", "True")
        # print(response)
        self.assertEqual(response.status_code, 200)

    def test_get_product_list(self):
        # response = requests.get(BASE)
        response = controller.get("6567815d30d2ff61bb2c625a", "False")
        self.assertEqual(response.status_code, 200)

    # TEST POST
    def test_post_product(self):
        # response = requests.post(f'{BASE}product/TEST/2/103000.0/TEST/Available')
        response = controller.post(name="TEST", amount=2, price=10300.0, description="TEST", status="Available")
        self.assertEqual(response.status_code, 200)

    def test_post_product_invalid_price(self):
        # response = requests.post(f'{BASE}product/TestProduct/10/%2D20.0/Test/Available')
        response = controller.post(name="TEST", amount=2, price=-10300.0, description="TEST", status="Available")
        self.assertEqual(response.status_code, 400)

    # TEST PUT
    def test_put_product(self):
        # response = requests.post(f'{BASE}product/6567815d30d2ff61bb2c625a/price/0.0')
        response = controller.put(id_product="6567815d30d2ff61bb2c625a", document={"price": 0.0})
        self.assertEqual(response.status_code, 200)

    def test_put_product_back(self):
        # response = requests.post(f'{BASE}product/6567815d30d2ff61bb2c625a/price/100.0')
        response = controller.put(id_product="6567815d30d2ff61bb2c625a", document={"price": 100.0})
        self.assertEqual(response.status_code, 200)

    # TEST DELETE
    def test_delete_product(self):
        response = controller.delete("65678310496d42c28392babb")
        self.assertEqual(response.status_code, 200 or 404)


if __name__ == '__main__':
    unittest.main()
