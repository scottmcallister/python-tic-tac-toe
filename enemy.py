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
    best_move = available_moves[0]  # TODO: get best move
    return best_move if len(available_moves) > 0 else [-1, -1]