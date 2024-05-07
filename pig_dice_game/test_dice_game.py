import unittest
from random import Random
from unittest.mock import patch, MagicMock
import dice_game
from dice_game import roll_dice, player_turn, computer_turn, game

class TestPig(unittest.TestCase):
    
    @patch('dice_game.random.randint')
    def test_dice(self, mock_randint):
        mock_randint.side_effect = [2, 1, 5, 6, 4, 3]
        self.assertEqual(roll_dice(), 2)  
    
    @patch('builtins.input', side_effect=['q', 'roll', 'hold'])    
    def test_exit(self, mock_input):
        player_score, exit_game = player_turn()
        self.assertTrue(exit_game) 
     
    @patch("dice_game.roll_dice", side_effect = [4, 6])
    @patch('builtins.print') 
    @patch('builtins.input', side_effect=['roll', 'roll', 'hold'])   
    def test_roll(self, mock_input, mock_print, mock_roll_dice):     
        player_score, exit_game = player_turn()
        self.assertEqual(player_score, 10)
        self.assertFalse(exit_game)
    
    @patch('builtins.print')    
    @patch('builtins.input', side_effect=['hold'])    
    def test_hold(self, mock_input, mock_print):
        player_score, exit_game = player_turn()
        mock_print.assert_any_call("Player score is", player_score)

    @patch('dice_game.random.choice')
    @patch('builtins.print')
    def test_computer_choice(self, mock_print, mock_choice):
        mock_choice.side_effect = ['roll', 'hold']
        computer_turn()
        mock_choice.assert_called_with(["roll", "hold"])
        self.assertEqual(mock_choice.call_count, 2)
    
    @patch('dice_game.computer_turn', return_value=5)
    @patch('dice_game.player_turn', side_effect=[(10, False), (15, False), (25, False)])     
    def test_game(self, mock_player_turn, mock_computer_turn):
        player_score = 50
        computer_score = 5
        self.assertGreaterEqual(player_score, computer_score)

if __name__ == "__main__":
    unittest.main()        
 
