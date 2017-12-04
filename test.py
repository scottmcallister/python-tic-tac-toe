import unittest
from utils import *


class TestSuite(unittest.TestCase):

    def test_check_for_win(self):
        x_win_state = [
            [' ', 'O', ' '],
            [' ', 'O', 'O'],
            ['X', 'X', 'X'],
        ]
        o_win_state = [
            [' ', 'O', ' '],
            [' ', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        playing_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        tie_state = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(check_for_win(x_win_state), 'X Wins!')
        self.assertEqual(check_for_win(o_win_state), 'O Wins!')
        self.assertEqual(check_for_win(playing_state), 'Active Game')
        self.assertEqual(check_for_win(tie_state), 'Tie')

    def test_no_blanks(self):
        has_blank_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        no_blank_state = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertTrue(no_blanks(no_blank_state))
        self.assertFalse(no_blanks(has_blank_state))

    def test_clone_board(self):
        some_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        self.assertEqual(clone_board(some_state), some_state)

    def test_check_rows(self):
        no_win_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        win_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(check_rows(win_state), 'X')
        self.assertEqual(check_rows(no_win_state), ' ')

    def test_check_cols(self):
        no_win_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        win_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(check_cols(win_state), 'O')
        self.assertEqual(check_cols(no_win_state), ' ')

    def test_check_diagonal(self):
        no_win_state = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        win_state = [
            ['O', 'X', ' '],
            [' ', 'O', ' '],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(check_diagonals(win_state), 'O')
        self.assertEqual(check_diagonals(no_win_state), ' ')


if __name__ == '__main__':
    unittest.main()
