import unittest
from quiz import question_one

class TestQuestions(unittest.TestCase):
    
    def test_question_one(self):
        self.assertTrue(question_one("mariana trench", "Correct answer"))
    
if __name__ == '__main__':
    unittest.main()        
    
"""question_one = input("1. What is the deepest ocean trench? ")
if question_one == "mariana trench":
    count += 1
    print("Correct!") 
else:
    print("Incorrect!")"""
