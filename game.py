import random

game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]
              ]


def ai_move(board):
    # possible_positions = available_positions(board)
    # random_spot = random.choice(possible_positions)

    spot = minimax(board, 0, False)

    # print("SPOT", spot)

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
            board[row][col] = 'x'
            score = minimax(board, depth + 1, False)
            board[row][col] = '_'

            # print("SCORE max", score, type(score))

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
            board[row][col] = 'o'
            score = minimax(board, depth + 1, True)
            board[row][col] = '_'

            # print("SCORE min", score, type(score))

            bestScore = min(score[0], bestScore)

            if bestScore == score[0]:
                bestMove = position
        return [bestScore, bestMove]


def evaluate(player):
    if player == 'x':
        return 1
    elif player == 'o':
        return -1
    else:
        return 0


def available_positions(board):
    available_pos = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                # print("in val")
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

    if board[x][y] in ['x', 'o']:
        return False

    if turn == 'x':
        board[x][y] = 'x'
    else:
        board[x][y] = 'o'
    return True


def check_win(board):
    # Row check
    for row in board:
        if row in [['x', 'x', 'x'], ['o', 'o', 'o']]:
            return True, row[0]

    # Column check
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] in ['x', 'o']:
            return True, board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] in ['x', 'o']:
            return True, board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] in ['x', 'o']:
            return True, board[0][2]

    # diagonal check
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] in ['x', 'o']:
            return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] in ['x', 'o']:
            return True, board[0][2]

    if len(available_positions(board)) == 0:
        return True, "draw"

    return False, ""


turn = 'x'
won = False

while not won:
    options = available_positions(game_board)
    game_visual = print_board(game_board)

    print(game_visual)

    if turn == 'x':
        print("Your options", options)
        pos = input("enter your position(row,col) player " + turn.upper() + ': ').split(' ')

        valid = enter_value(game_board, pos, turn)
        if valid:
            turn = 'o'
        else:
            print("Space is taken. Try again.")
    else:
        ai_choice = ai_move(game_board)
        print("AI played at", ai_choice)
        valid = enter_value(game_board, ai_choice, turn)
        if valid:
            turn = 'x'
        else:
            print("Space is taken. Try again.")

    won, player_won = check_win(game_board)

    if won and player_won != "draw":
        winning_board = print_board(game_board)
        print("Congratulations player", player_won.upper(), "won!", won)
        print(winning_board)
    elif player_won == "draw":
        print("GAME IS A DRAW!!")
