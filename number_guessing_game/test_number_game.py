#tests: will use mocking and patch testing due to user and print statements
#test 1: if top number is less than 0
#test 2: top number isdigit
#test 3: if random number prints out 1 number
#test 4: user guesses return 1 work for user_guess > number:
#test 5: user guesses return 1 work for user_guess < number:
#test 6: user guess == number gueses return 1

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
    
if __name__ == "__main__":
    unittest.main()  
    
    
    