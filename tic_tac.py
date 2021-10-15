import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

won = False

while not won:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            won = True

    screen.fill('blue')
    pygame.display.flip()

pygame.quit()

