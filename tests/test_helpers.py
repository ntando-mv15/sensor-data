import unittest
from unittest.mock import patch
from app.helpers import fetch_temperature_from_box

class TestHelpers(unittest.TestCase):
    @patch("helpers.requests.get")
    def test_fetch_temperature_success(self, mock_get):
        # Mocking a sample successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "sensors": [
                {
                    "title": "Temperatur",
                    "lastMeasurement": {
                        "value": "23.5",
                        "createdAt": "2025-04-13T12:30:00.000Z"
                    }
                }
            ]
        }

        result = fetch_temperature_from_box("dummy_id")
        self.assertEqual(result, 23.5)

    @patch("helpers.requests.get")
    def test_fetch_temperature_no_temp(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"sensors": []}

        result = fetch_temperature_from_box("dummy_id")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
