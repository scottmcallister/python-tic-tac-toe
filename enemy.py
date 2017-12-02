from utils import clone_board, check_for_win


def get_move(board_state):
    available_moves = []
    claimed_by_x = []
    claimed_by_o = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board_state[row][col] == ' ':
                available_moves.insert(0, [row, col])
            elif board_state[row][col] == 'O':
                claimed_by_o.insert(0, [row, col])
            elif board_state[row][col] == 'X':
                claimed_by_x.insert(0, [row, col])
    if len(available_moves) == 0:
        return [-1, -1]
    move_scores = []
    for move in available_moves:
        current_score = 0
        new_board = clone_board(board_state)
        # check for winning move
        new_board[move[0]][move[1]] = 'X'
        if check_for_win(new_board) != 'Active Game':
            return move
        # prevent player from winning
        new_board[move[0]][move[1]] = 'O'
        if check_for_win(new_board) != 'Active Game':
            return move
        # threaten win if possible
        new_board[move[0]][move[1]] = 'X'
        win_moves = count_win_moves(new_board)
        if win_moves > 0:
            current_score += win_moves * 10
        # take middle if available
        if move == [1, 1]:
            current_score += 5
        # take corner if available
        if move[0] != 1 and move[1] != 1:
            current_score += 3
        move_scores.append(current_score)
    best_move_score = max(move_scores)
    for i in range(0, len(available_moves)):
        if move_scores[i] == best_move_score:
            return available_moves[i]


def count_win_moves(board_state):
    available_moves = []
    winning_moves = 0
    for row in range(0, 3):
        for col in range(0, 3):
            if board_state[row][col] == ' ':
                available_moves.insert(0, [row, col])
    for move in available_moves:
        new_board = clone_board(board_state)
        new_board[move[0]][move[1]] = 'X'
        if check_for_win(new_board) == 'X Wins!':
            winning_moves += 1
    return winning_moves
