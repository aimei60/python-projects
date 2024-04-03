import unittest
from unittest.mock import patch
from game import computer_guess, game

class TestGame(unittest.TestCase):
    
    def test_randomness_computer_choice(self):
        choices = {computer_guess() for i in range(10)}
        self.assertTrue(len(choices) > 1)
    
    @patch('builtins.input', side_effect=["rock", "paper", "scissors", "rock", "paper", "scissors"])  
    @patch('builtins.print')  
    def test_computer_win(self, mock_print, mock_input):
        with patch('random.choice', side_effect=["paper", "scissors", "rock", "paper", "scissors", "rock"]):
            game()
        mock_print.assert_called_with("Sorry you lost, Computer wins!")
            
    @patch('builtins.input', side_effect=["rock", "paper", "scissors", "rock", "paper", "scissors"])
    @patch('builtins.print')
    def test_user_win(self, mock_print, mock_input):
        with patch('random.choice', side_effect=["scissors", "rock", "paper", "scissors", "rock", "paper"]):
            game() 
        mock_print.assert_called_with("Congratulations, you win! You have beat the Computer!") 
    
if __name__ == '__main__':
    unittest.main()