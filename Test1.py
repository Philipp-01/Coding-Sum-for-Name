import unittest
from SumForName import numbersum

class TestSumForName(unittest.TestCase):

    def test_sumforname(self):
        self.assertEqual(numbersum)

if __name__ == '__main__':
    unittest.main()