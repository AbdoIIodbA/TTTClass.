import unittest
import TTTclass

class TestTTTclass(unittest.TestCase):

    def test_is_winner(self):
        self.assertEqual(TTTclass.is_winner([[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9],[3,5,7]]), True)
