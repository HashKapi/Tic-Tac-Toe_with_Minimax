import sys

import pygame
import game

# Global constants
logic_board = [["_", "_", "_"],
               ["_", "_", "_"],
               ["_", "_", "_"]]
WIDTH = 600
HEIGHT = 600
BOX_SIZE = (WIDTH // 3)

myFont, winningFont = None, None

won = False
turn = 'X'
state = ''


def draw_lines(screen_a):
    """
    Draws the vertical and horizontal lines on the screen
    :param screen_a: game screen which is the variable screen
    :return:
    """
    for vertical_line in range(BOX_SIZE, WIDTH, BOX_SIZE):
        pygame.draw.line(screen_a, (128, 0, 0), (vertical_line, 0), (vertical_line, HEIGHT), width=1)

    for horizontal_line in range(BOX_SIZE, WIDTH, BOX_SIZE):
        pygame.draw.line(screen_a, (128, 0, 0), (0, horizontal_line), (HEIGHT, horizontal_line), width=1)


def draw_XO(screen_a):
    """
    Draws the X's and O's on the screen
    :param screen_a: game screen which is the variable screen
    :return:
    """
    for col in range(0, 3):
        y = col * BOX_SIZE
        for row in range(0, 3):
            letter = myFont.render(logic_board[col][row], False, (0, 0, 0))
            x = (row * BOX_SIZE) + 20
            screen_a.blit(letter, (x, y))


def add_XO(x, y):
    """
    Adds the user's input and checks whether the game is won or drawn
    :param x: x position from the player's mouseclick
    :param y: y position from the player's mouseclick
    :return:
    """
    global turn, won, state
    available_positions = game.available_positions(logic_board)
    if [x, y] in available_positions:
        valid = game.enter_value(logic_board, [x, y], turn)

        if valid:
            spots_after_play = len(game.available_positions(logic_board))
            if turn == 'X' and spots_after_play > 0:
                turn = 'O'
                ai_choice = game.ai_move(logic_board)
                valid = game.enter_value(logic_board, ai_choice, turn)
                if valid:
                    turn = 'X'

    win_value, player_won = game.check_win(logic_board)
    if win_value:
        won = True
        state = player_won


def win_screen(screen_a):
    """
    Draws win screen if there is a draw or winner
    :param screen_a: game screen which is the variable screen
    :return:
    """
    global won, state

    if won and state != "draw":
        if turn == 'X':
            text = winningFont.render("AI Wins", False, (255, 0, 0))
        else:
            text = winningFont.render("Player wins!!", False, (255, 0, 0))
        screen_a.blit(text, (100, 200))
    elif state == 'draw':
        text = winningFont.render("Game is a draw!", False, (255, 0, 0))
        screen_a.blit(text, (100, 200))


def main():
    global myFont, winningFont

    pygame.init()

    myFont = pygame.font.SysFont('Comic Sans MS', 150)
    winningFont = pygame.font.SysFont('Comic Sans MS', 50)

    fps = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                y, x = pygame.mouse.get_pos()

                x = x // BOX_SIZE
                y = y // BOX_SIZE

                if not won:
                    add_XO(x, y)

        screen.fill('white')
        draw_lines(screen)
        draw_XO(screen)
        win_screen(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
