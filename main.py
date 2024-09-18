import pygame

import player
from constants import *

def main():
    screen_x_middle = SCREEN_WIDTH / 2
    screen_y_middle = SCREEN_HEIGHT / 2

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    player1 = player.Player(screen_x_middle, screen_y_middle)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player1.draw(screen)
        pygame.display.flip()
        dt += game_clock.tick(60) / 1000
   


if __name__ == "__main__":
    main()
