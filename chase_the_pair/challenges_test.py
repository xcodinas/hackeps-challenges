import unittest
from challenges import close_pair


class TestChallenges(unittest.TestCase):

    def test_chase_the_pair(self):
        a = [1, 23, 45, 66, 84, 113, 145, 178, 205, 210, 221, 250, 264, 300]
        b = [5, 31, 40, 52, 73, 103, 126, 162, 195, 214, 225, 241, 256, 267]
        self.assertEqual(close_pair(a, b, 231), [221, 225],
            "Should be [221, 225]")

if __name__ == '__main__':
    unittest.main()
