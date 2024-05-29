import unittest
from unittest import mock
from weather import get_API

class TestWeatherAPI(unittest.TestCase):
    @mock.patch("requests.get")
    def test_get_API(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {"temp": 298.15},  # Example temperature in Kelvin (25°C)
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response
        get_API()
           
if __name__ == "__main__":
    unittest.main()

