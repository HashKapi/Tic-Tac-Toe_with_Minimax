def ai_move(board):
    spot = minimax(board, 0, False)

    return spot[1]


def minimax(board, depth, max_player):
    win = check_win(board)
    if win[0]:
        return [evaluate(win[1]), None]

    if max_player:
        bestScore = float('-inf')
        bestMove = None
        playable_positions = available_positions(board)

        for position in playable_positions:
            row, col = position[0], position[1]
            board[row][col] = 'X'
            score = minimax(board, depth + 1, False)
            board[row][col] = '_'

            bestScore = max(score[0], bestScore)

            if bestScore == score[0]:
                bestMove = position
        return [bestScore, bestMove]
    else:
        bestScore = float('inf')
        bestMove = None
        playable_positions = available_positions(board)

        for position in playable_positions:
            row, col = position[0], position[1]
            board[row][col] = 'O'
            score = minimax(board, depth + 1, True)
            board[row][col] = '_'


            bestScore = min(score[0], bestScore)

            if bestScore == score[0]:
                bestMove = position
        return [bestScore, bestMove]


def evaluate(player):
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    else:
        return 0


def available_positions(board):
    available_pos = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                empty_slot = [row, col]
                available_pos.append(empty_slot)
    return available_pos


def print_board(board):
    blueprint = ''
    for row in board:
        for val in row:
            blueprint += val + '|'
        blueprint += '\n'

    return blueprint


def enter_value(board, pos, turn):
    x, y = int(pos[0]), int(pos[1])

    if board[x][y] in ['X', 'O']:
        return False

    if turn == 'X':
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'
    return True


def check_win(board):
    # Row check
    for row in board:
        if row in [['X', 'X', 'X'], ['O', 'O', 'O']]:
            return True, row[0]

    # Column check
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] in ['X', 'O']:
            return True, board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] in ['X', 'O']:
            return True, board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] in ['X', 'O']:
            return True, board[0][2]

    # diagonal check
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] in ['X', 'O']:
            return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] in ['X', 'O']:
            return True, board[0][2]

    if len(available_positions(board)) == 0:
        return True, "draw"

    return False, ""

