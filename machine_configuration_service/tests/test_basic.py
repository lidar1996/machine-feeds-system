import unittest
from machine_configuration_service.app import create_app

class MachineConfigurationRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_get_machine_configuration_by_id(self):
        response = self.client.get('/machine_configurations/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('data', data)

if __name__ == '__main__':
    unittest.main()
