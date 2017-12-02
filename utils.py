def check_for_win(board_state):
    if check_rows(board_state) != ' ':
        return check_rows(board_state) + " Wins!"
    if check_cols(board_state) != ' ':
        return check_cols(board_state) + " Wins!"
    if check_diagonals(board_state) != ' ':
        return check_cols(board_state) + " Wins!"
    if no_blanks(board_state):
        return 'Tie'
    return 'Active Game'


def check_rows(board_state):
    for row in range(0, 3):
        row_vals = board_state[row]
        if all(cell == row_vals[0] for cell in row_vals) \
           and board_state[row][0] != ' ':
            return board_state[row][0]
    return ' '


def check_cols(board_state):
    for col in range(0, 3):
        col_vals = [
            board_state[0][col],
            board_state[1][col],
            board_state[2][col]
        ]
        if all(cell == board_state[0][col] for cell in col_vals) \
           and board_state[0][col] != ' ':
            return board_state[0][col]
    return ' '


def check_diagonals(board_state):
    descending = [
        board_state[0][0],
        board_state[1][1],
        board_state[2][2]
    ]
    ascending = [
        board_state[2][0],
        board_state[1][1],
        board_state[0][2]
    ]
    if all(cell == descending[0] for cell in descending) \
       and descending[0] != ' ':
        return descending[0]
    if all(cell == ascending[0] for cell in ascending) \
       and ascending[0] != ' ':
        return ascending[0]
    return ' '


def no_blanks(board_state):
    for row in range(0, 3):
        for col in range(0, 3):
            if board_state[row][col] == ' ':
                return False
    return True


def clone_board(board_state):
    new_board = []
    for row in range(0, 3):
        new_row = []
        for col in range(0, 3):
            new_row.append(board_state[row][col])
        new_board.append(new_row)
    return new_board
