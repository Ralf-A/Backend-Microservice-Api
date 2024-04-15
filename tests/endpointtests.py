# Python code for unit testing the Flask API
import unittest

# Add the server directory to sys.path
from server.server import app


class NetworkTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # Test to get all interfaces
    def test_get_all_interfaces(self):
        response = self.client.get('/network')
        self.assertEqual(response.status_code, 200)

    # Test to get a specific interface, change this to the interface you want to test
    def test_get_specific_interface(self):
        response = self.client.get('/network?interface=lan')
        self.assertEqual(response.status_code, 200)

    # Test to get an interface that does not exist, change this to an interface that does not exist if needed :D
    def test_interface_not_found(self):
        response = self.client.get('/network?interface=fake_interface')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
