import unittest
from repair_service.app import create_app

class RepairServiceRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_get_repairs_by_id(self):
        response = self.client.get('/repairs/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()[0]
        self.assertIn('data', data)

if __name__ == '__main__':
    unittest.main()
