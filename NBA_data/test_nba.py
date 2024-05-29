import unittest
from unittest import mock
from nba import get_scoreboard, get_game_date
from unittest.mock import patch


class TestNBAData(unittest.TestCase):
    @mock.patch("requests.get")
    def test_get_scoreboard(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "scoreboard": {
                "gameDate": "2024-05-29",
                "games": [
                    {"homeTeam": "Tigers", "awayTeam": "Bears", "time": "12pm CET"}
                ]
            }
        }
        mock_get.return_value = mock_response
        scoreboard = get_scoreboard()
        
        self.assertEqual(scoreboard["gameDate"], "2024-05-29")
        self.assertEqual(scoreboard["games"][0]["homeTeam"], "Tigers")
        self.assertEqual(scoreboard["games"][0]["awayTeam"], "Bears")
        self.assertEqual(scoreboard["games"][0]["time"], "12pm CET")
        
        
    @mock.patch("requests.get")
    @patch('builtins.print')
    def test_get_game_date(self, mock_print, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200  
        mock_response.json.return_value = {
            "scoreboard": {
                "gameDate": "2024-05-29"
            }
        }
        
        mock_get.return_value = mock_response  
        get_game_date()
        mock_print.assert_called_with('2024-05-29')
    
if __name__ == "__main__":
    unittest.main()   