import unittest
from unittest.mock import patch
from datetime import datetime, timezone, timedelta
from app.helpers import fetch_temperature_from_box

def recent_timestamp():
    recent_time = datetime.now(timezone.utc) - timedelta(minutes=30)
    return recent_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

class TestHelpers(unittest.TestCase):
    @patch("app.helpers.requests.get")
    def test_fetch_temperature_success(self, mock_get):
        # Mocking a sample successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "sensors": [
                {
                    "title": "Temperatur",
                    "lastMeasurement": {
                        "value": "23.5",
                        "createdAt": recent_timestamp()
                    }
                }
            ]
        }

        result = fetch_temperature_from_box("dummy_id")
        self.assertEqual(result, 23.5)

if __name__ == "__main__":
    unittest.main()
