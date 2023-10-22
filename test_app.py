import unittest
from main import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_report(self):
        response = self.app.get('/api/report/test_report?from=2021-01-01&to=2021-12-31')
        self.assertEqual(response.status_code, 200)

    def test_get_last_seen(self):
        response = self.app.get('/api/users/last_seen?offset=0')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
