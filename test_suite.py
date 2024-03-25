import unittest
import threading
from unittest.mock import patch
from main import MyServer
from http.server import HTTPServer
from urllib.request import urlopen
import json


class TestMyServer(unittest.TestCase):

    def setUp(self):
        self.server = HTTPServer(('localhost', 8080), MyServer)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server_thread.join()

    def test_post_request_valid_token(self):
        response = urlopen('http://localhost:8080/auth')
        data = response.read().decode('utf-8')
        decoded_data = json.loads(data)
        self.assertIn('exp', decoded_data)
        self.assertIsInstance(decoded_data['exp'], int)

    def test_post_request_expired_token(self):
        response = urlopen('http://localhost:8080/auth?expired=true')
        data = response.read().decode('utf-8')
        decoded_data = json.loads(data)
        self.assertIn('exp', decoded_data)
        self.assertIsInstance(decoded_data['exp'], int)
        self.assertLess(decoded_data['exp'], int(datetime.datetime.utcnow().timestamp()))

    def test_get_request_jwks_json(self):
        response = urlopen('http://localhost:8080/.well-known/jwks.json')
        data = response.read().decode('utf-8')
        decoded_data = json.loads(data)
        self.assertIn('keys', decoded_data)
        self.assertIsInstance(decoded_data['keys'], list)
        self.assertEqual(len(decoded_data['keys']), 1)
        self.assertIn('n', decoded_data['keys'][0])
        self.assertIn('e', decoded_data['keys'][0])
        self.assertIn('kid', decoded_data['keys'][0])

    def test_invalid_path(self):
        response = urlopen('http://localhost:8080/invalid')
        self.assertEqual(response.status, 405)

if __name__ == '__main__':
    unittest.main()
