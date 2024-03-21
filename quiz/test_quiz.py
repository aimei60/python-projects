import unittest
from unittest.mock import patch
from unittest.mock import call
from quiz import questions, quiz 

class TestQuizGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["mariana trench", "greenland", "harper lee", "scoville scale", "canberra"])
    @patch('builtins.print')
    def test_quiz_all_correct(self, mock_print, mock_input):
        quiz()
        #test for mock print
        mock_print.assert_any_call("Your score is:", 5, "out of 5")
        mock_print.assert_any_call("The percentage of your score is", 100.0, "%")
        #test for mock input
        question_calls = [call("1. What is the deepest ocean trench? "),
                call("2. What is the largest island in the world? "),
                call("3. Who wrote the famous novel To Kill a Mockingbird? "),
                call("4. What is the name of the scale used to measure spiciness of peppers? "),
                call("5. What is the capital of Australia? ",)
                ]
        mock_input.assert_has_calls(question_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
