import unittest
from unittest.mock import mock_open, patch
import manager
from manager import manager, load_key

class TestPasswordManager(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data=b'Kgh58dhafGGb9thd')
    def test_load_key(self, mock_file):
        with open('key.key', 'rb') as f:
            result = f.read()
        mock_file.assert_called_once_with('key.key', 'rb')
        self.assertEqual(result, b'Kgh58dhafGGb9thd')
    
    @patch('builtins.open', new_callable=mock_open)
    @patch("builtins.input", side_effect=['asos', 'iloveshopping'])
    def test_add(self, mock_input, mock_file):
        mock_input.return_value = 'asos'
        mock_input.return_value = 'iloveshopping'
        with open('password.txt', 'w') as l:
            l.write('asos | iloveshopping')
        mock_file.mock_calls
        mock_file.assert_called_once_with('password.txt', 'w')
        mock_file().write.assert_called_once_with('asos | iloveshopping')
    
    @patch("manager.add")
    @patch("builtins.input", side_effect=['add', 'q'])
    def test_option_add(self, mock_input, mock_add):
        manager.manager()
        mock_add.assert_called_once()
        
    @patch("manager.view")
    @patch("builtins.input", side_effect=['view', 'q'])
    def test_option_add(self, mock_input, mock_view):
        manager()
        mock_view.assert_called_once()
    
    @patch("builtins.print") 
    @patch("builtins.input", side_effect=['q'])   
    def test_break(self, mock_input, mock_print):
        manager()
        mock_print.assert_called_with('Exiting Password Manager')
        
        
if __name__ == "__main__":
    unittest.main()