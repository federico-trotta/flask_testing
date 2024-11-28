import unittest
import sys
import os

# Add the parent directory to sys.path to import app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestAppIntegration(unittest.TestCase):
    """Integration tests for the Flask application."""

    def setUp(self):
        """Set up the test client."""
        # Configure the app for testing
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add_endpoint(self):
        """Test the /add endpoint with valid and invalid inputs."""
        # Valid input test
        response = self.client.get('/add?a=10&b=20')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 30.0})

        # Invalid input test (non-numeric values)
        response = self.client.get('/add?a=foo&b=bar')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

        # Missing parameter test (missing 'b')
        response = self.client.get('/add?a=10')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

    def test_multiply_endpoint(self):
        """Test the /multiply endpoint with valid and invalid inputs."""
        # Valid input test
        response = self.client.get('/multiply?a=5&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 20.0})

        # Invalid input test (non-numeric value for 'b')
        response = self.client.get('/multiply?a=5&b=bar')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

        # Missing parameter test (missing 'b')
        response = self.client.get('/multiply?a=5')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

    def test_add_multiply_endpoint(self):
        """Test the /add_multiply endpoint with valid and invalid inputs."""
        # Valid input test
        response = self.client.get('/add_multiply?a=2&b=3&c=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 20.0})  # (2 + 3) * 4 = 20

        # Invalid input test (non-numeric value for 'a')
        response = self.client.get('/add_multiply?a=foo&b=3&c=4')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

        # Missing parameter test (missing 'c')
        response = self.client.get('/add_multiply?a=2&b=3')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input'})

    def test_calculate_route(self):
        """Test the /calculate route for form submissions."""
        # Test addition via form submission
        response = self.client.post('/calculate', data={
            'operation': 'add',
            'a': '5',
            'b': '7'
        })
        self.assertIn(b'The result is: 12.0', response.data)

        # Test multiplication via form submission
        response = self.client.post('/calculate', data={
            'operation': 'multiply',
            'a': '4',
            'b': '6'
        })
        self.assertIn(b'The result is: 24.0', response.data)

        # Test add and multiply via form submission
        response = self.client.post('/calculate', data={
            'operation': 'add_multiply',
            'a': '2',
            'b': '3',
            'c': '5'
        })
        self.assertIn(b'The result is: 25.0', response.data)

        # Test invalid input via form submission
        response = self.client.post('/calculate', data={
            'operation': 'add',
            'a': 'foo',
            'b': 'bar'
        })
        self.assertIn(b'Error: Invalid input provided.', response.data)

if __name__ == '__main__':
    unittest.main()