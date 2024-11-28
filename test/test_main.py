import unittest
import main

class TestMainWordle(unittest.TestCase):

    def setUp(self):
        self.main = main

    """def test_guess(self):
        self.assertEqual(self.main.score_guess("world", "world"), [2, 2, 2, 2, 2])

    def test_no_match(self):
        self.assertEqual(self.main.score_guess("world", "hello"), [0, 0, 0, 0, 0])"""

    def test_guess(self):
        self.assertEqual(self.main.score_guess("world", "world"), [2, 2, 2, 2, 2])

    def test_no_match(self):
        self.assertEqual(self.main.score_guess("world", "hello"), [0, 1, 0, 2, 0])

    def test_completion_message(self):
        self.assertEqual(self.main.completion_message(True), "CONGRATULATIONS YOU HAVE WON!")

    def test_losing_message(self):
        self.main.target = "world"
        self.assertEqual(self.main.completion_message(False), f"Sorry, you lost! The word was [{self.main.target}]")
