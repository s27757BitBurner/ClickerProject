import unittest
from flask_testing import TestCase
from app import app, score

class ClickerGameTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b'Score: 0', response.data)
        self.assertIn(b'Click me!', response.data)

    def test_click_endpoint(self):
        global score
        score = 0
        initial_score = score

        response = self.client.post('/click')
        self.assert200(response)
        self.assertEqual(response.json['score'], initial_score + 1)
        response = self.client.post('/click')
        self.assertEqual(response.json['score'], initial_score + 2)

    def test_score_persistence(self):
        global score
        score = 0

        self.client.post('/click')
        self.client.post('/click')
        self.client.post('/click')
        response = self.client.post('/click')

        self.assertEqual(response.json['score'], 6)

if __name__ == '__main__':
    unittest.main()
