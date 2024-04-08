import unittest
import io
import sys
from unittest.mock import patch, MagicMock
from unittest import mock
from converter import converter

class TestCurrencyConverter(unittest.TestCase):

        @mock.patch("Client.latest")
        def test_converter_function(self, mock_latest):
            mock_latest.return_value("data': {'GBP': {'code': 'GBP', 'value': 0.7919601282}")
            myOutput = io.StringIO()
            sys.stdout = myOutput
            converter()
            sys.stdout = sys.__stdout__
            self.assertIn("'GBP': {'code': 'GBP', 'value': 0.7919601282", myOutput.getvalue())

print(sys.path)         
if __name__ == "__main__":
    unittest.main()