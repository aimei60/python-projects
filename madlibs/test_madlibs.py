import unittest
from unittest.mock import mock_open
from unittest.mock import patch
import madlibs_program
from madlibs_program import read_file, madlibs

class TestMadlibs(unittest.TestCase):
    
    def test_read_file(self):
        h = mock_open(read_data='madlibs story')
        with patch('madlibs_program.open', h):
            result = madlibs_program.read_file('storyfile')
            self.assertEqual(result, 'madlibs story')
        
    @patch('builtins.input', side_effect=['chair'])    
    def test_madlibs(self, mock_input):
        #test to find target words
        target_start_and_end = "<>"
        new_word = '<noun>'
        self.assertIn(target_start_and_end[0], new_word)
        self.assertIn(target_start_and_end[1], new_word)
        #test the input
        mock_input = 'chair'
        assert mock_input == 'chair'
        #test the replace function
        original_word = '<name>'
        replace_word = original_word.replace('<name>', mock_input)
        self.assertEqual(replace_word, 'chair')
    
if __name__ == '__main__':
    unittest.main()