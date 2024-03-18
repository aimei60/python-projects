import unittest
from unittest.mock import patch
from quiz import questions, quiz 

class TestQuizGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["mariana trench", "greenland", "harper lee", "scoville scale", "canberra"])
    @patch('builtins.print')
    def test_quiz_all_correct(self, mock_print, mock_input):
        quiz()
        mock_print.assert_any_call("Your score is:", 5, "out of 5")
        mock_print.assert_any_call("The percentage of your score is", 100.0, "%")
        #test for mock input


if __name__ == '__main__':
    unittest.main()
