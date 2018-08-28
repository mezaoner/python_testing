import unittest

import c_moves


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = c_moves.Rock()
        self.scissors = c_moves.Scissors()
        self.paper = c_moves.Paper()

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

    def test_equal(self):
        self.assertEqual(self.rock, c_moves.Rock())

    def test_not_equal(self):
        rock = c_moves.Rock()
        paper = c_moves.Paper()
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worse_scissors(self):
        self.assertLess(self.paper, self.scissors)

if __name__ == "__main__":
    unittest.main()
