import unittest
from unittest.mock import patch
from app.main import app  

class TestMainEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_version(self):
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertIn("App version", response.get_json())

    @patch("app.main.fetch_temperature_from_box")  
    def test_temperature(self, mock_temp_func):
        mock_temp_func.side_effect = [20.5, 21.0, None]
        response = self.client.get("/temperature")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("average_temperature", data)
        self.assertAlmostEqual(data["average_temperature"], 20.75, places=2)

    @patch("app.main.fetch_temperature_from_box") 
    def test_temperature_no_data(self, mock_temp_func):
        mock_temp_func.return_value = None
        response = self.client.get("/temperature")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()

    