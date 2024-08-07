import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_negotiate(self):
        response = self.client.post('/negotiate', json={
            'input_text': 'I want to buy this product',
            'product_id': 1,
            'user_id': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json)

    def test_order(self):
        response = self.client.post('/order', json={
            'product_id': 1,
            'user_id': 1,
            'price': 99.99
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json)

if __name__ == '__main__':
    unittest.main()
