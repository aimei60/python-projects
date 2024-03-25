import unittest
from number_game import numbers, game
from unittest.mock import patch 

class TestQuiz(unittest.TestCase):
    @patch('builtins.input', side_effect=["not a number", "10"])
    @patch('builtins.print')
    def test_top_number(self, mock_print, mock_input):
        numbers()
        mock_print.assert_any_call("Incorrect value, please enter a number bigger than 0")
    
    @patch('builtins.input', return_value='10')
    @patch("number_game.random.randrange", return_value=5)    
    def test_random_number_to_return(self, mock_randrange, mock_input):
        expected_random_number = 5
        result = numbers() #check calling numbers works
        self.assertEqual(result, expected_random_number)
        mock_randrange.assert_called_once_with(1, 11)
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['7', '6'])
    def test_guess_too_high(self, mock_input, mock_print):
        with patch('number_game.number', new=6):
            game()
        mock_print.assert_any_call("Your number is too high, guess again!")
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '6'])
    def test_guess_too_low(self, mock_input, mock_print):
        with patch('number_game.number', new=6):
            game()
        mock_print.assert_any_call("Your number is too low, guess again!")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['6'])
    def test_correct_guess(self, mock_input, mock_print):
        with patch('number_game.number', new=6):
            game()
        mock_print.assert_called_with("You guessed correct! You guessed in 1 guesses!")


if __name__ == "__main__":
    unittest.main()  
    
    
    