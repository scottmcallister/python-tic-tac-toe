import unittest
from utils import *
from main import move_up, move_down, move_left, move_right
from enemy import *


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

    def test_move_up(self):
        top_row_pos = 0
        bottom_row_pos = 8
        self.assertEqual(move_up(top_row_pos), 0)
        self.assertEqual(move_up(bottom_row_pos), 5)

    def test_move_down(self):
        top_row_pos = 0
        bottom_row_pos = 8
        self.assertEqual(move_down(top_row_pos), 3)
        self.assertEqual(move_down(bottom_row_pos), 8)
        
    def test_move_left(self):
        left_col_pos = 0
        right_col_pos = 8
        self.assertEqual(move_left(left_col_pos), 0)
        self.assertEqual(move_left(right_col_pos), 7)
        
    def test_move_right(self):
        left_col_pos = 0
        right_col_pos = 8
        self.assertEqual(move_right(left_col_pos), 1)
        self.assertEqual(move_right(right_col_pos), 8)

    def test_get_move(self):
        win_opportunity = [
            ['O', ' ', ' '],
            ['O', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        block_opportunity = [
            ['O', ' ', ' '],
            ['O', 'X', ' '],
            [' ', ' ', ' '],
        ]
        center_opportunity = [
            ['O', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.assertEqual(get_move(win_opportunity), [2, 1])
        self.assertEqual(get_move(block_opportunity), [2, 0])
        self.assertEqual(get_move(center_opportunity), [1, 1])

    def test_count_win_moves(self):
        win_opportunity = [
            ['O', ' ', ' '],
            ['O', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        multi_win_opportunity = [
            ['O', 'O', 'X'],
            ['O', 'O', ' '],
            ['X', ' ', 'X'],
        ]
        self.assertEqual(count_win_moves(win_opportunity), 1)
        self.assertEqual(count_win_moves(multi_win_opportunity), 2)


if __name__ == '__main__':
    unittest.main()
