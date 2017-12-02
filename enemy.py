def get_move(board_state):
    available_moves = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board_state[row][col] == ' ':
                available_moves.insert(0, [row, col])
    return available_moves[0] if len(available_moves) > 0 else [-1, -1]