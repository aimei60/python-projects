import unittest
from generator import password_generator

class TestPasswordGenerator(unittest.TestCase):
    def test_randomness(self):
        passwords = {password_generator(10) for i in range(50)}
        self.assertTrue(len(passwords) > 1)
    
    def test_correct_length(self):
        length = 10
        password = password_generator(10)
        self.assertEqual(length, len(password))
        
if __name__ == "__main__":
    unittest.main()