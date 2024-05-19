import unittest
import random
from unittest.mock import patch, call
import slotmachine
from slotmachine import slot_choices, slot_game

class TestSlotMachine(unittest.TestCase):
    
    @patch('machine.random.choice')
    def test_slot_choices(self, mock_random_choice):
        mock_random_choice.side_effect = ["seven", "gold bar", "cherry"]
        self.assertEqual(slot_choices(), "seven gold bar cherry")
    
    @patch('machine.slot_choices')
    @patch('builtins.print')
    @patch('builtins.input', return_value='10')        
    def test_cherry_win(self, mock_input, mock_print, mock_slot_choices):
        mock_slot_choices.return_value = "cherry cherry cherry"
        
        slot_game()
        
        calls = [
            call("Welcome to the slot machine game! It costs only £10 to play for each go!"),
            call("Here are the prizes: \n 3 cherry's: £500 \n 3 seven's: £1,000 \n 3 gold bars: £10,000"),
            call("cherry cherry cherry"),
            call("Congratulations you win £500! Your total amount is £510"),
        ]
        
        mock_print.assert_has_calls(calls, any_order=True)
        
    @patch('machine.slot_choices')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['20', 'continue', 'quit'])
    def test_score_loss(self, mock_input, mock_print, mock_slot_choice):
        mock_slot_choice.return_value = "seven gold bar cherry"
        slot_game()
        mock_print.assert_any_call("Sorry no wins this time! Your score is £10")
        calls = [
            call("Do you want to continue or quit the game? "),
            call('Enter how much you want to play with: ')
            ]
        mock_input.assert_has_calls(calls, any_order=True)
       
        