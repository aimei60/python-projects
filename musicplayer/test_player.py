import unittest
from unittest.mock import patch
from unittest.mock import call
from player import music, play_music

class TestMusicPlayer(unittest.TestCase):
    
    @patch('player.pygame.mixer.music.load')
    @patch('player.pygame.mixer.music.play')
    @patch('pygame.mixer.music.get_busy')
    def test_music(self, mock_get_busy, mock_play, mock_load):
        mock_get_busy.side_effect=[True, False]
        music("tune.mp3")
        mock_load.assert_called_once_with('tune.mp3')
        mock_play.assert_called_once()
        self.assertTrue(mock_get_busy.called)
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_wrong_choice(self, mock_print, mock_input):
        #test for wrong music choice
        mock_print.return_value = 'metal'
        play_music()
        mock_print.assert_called_once_with("Your choice is invalid to play music")
    
if __name__ == "__main__":
    unittest.main()
        
        
        