import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import suma

class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)

if __name__ == '__main__':
    unittest.main()