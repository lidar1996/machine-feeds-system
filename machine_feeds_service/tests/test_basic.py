import unittest
from unittest.mock import patch
from machine_feeds_service.app.controllers.machine_feeds_controller import fetch_combined_feeds
from machine_feeds_service.app import create_app

class FetchCombinedFeedsTest(unittest.TestCase):
    def setUp(self):
        # Create and configure app context
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Clean up app context
        self.app_context.pop()

    @patch('machine_feeds_service.app.controllers.machine_feeds_controller.get_sessions')
    @patch('machine_feeds_service.app.controllers.machine_feeds_controller.get_repairs')
    @patch('machine_feeds_service.app.controllers.machine_feeds_controller.get_machine_configuration')
    def test_fetch_combined_feeds_success(self, mock_get_config, mock_get_repairs, mock_get_sessions):
        # Mock return values
        mock_get_config.return_value = {"id": "1"}
        mock_get_repairs.return_value = [{"id": 1, "machine_id": 1, "created_at": "2023-01-01T12:00:00"}]
        mock_get_sessions.return_value = [{"id": 2, "machine_id": 1, "created_at": "2023-01-02T12:00:00"}]

        # Call the function
        response, status_code = fetch_combined_feeds("1")

        # Validate response
        self.assertEqual(status_code, 200)
        data = response.get_json()
        self.assertIn("machine_configuration", data)
        self.assertEqual(len(data["activities"]), 2)
        self.assertEqual(data["activities"][0]["type"], "session")
        self.assertEqual(data["activities"][1]["type"], "repair")

    @patch('machine_feeds_service.app.controllers.machine_feeds_controller.get_machine_configuration')
    def test_fetch_combined_feeds_not_found(self, mock_get_config):
        mock_get_config.return_value = {"error": "Machine not found"}
        response, status_code = fetch_combined_feeds("999")

        self.assertEqual(status_code, 404)
        self.assertIn("error", response.get_json())

if __name__ == '__main__':
    unittest.main()
