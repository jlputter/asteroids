import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    screen_x_middle = SCREEN_WIDTH / 2
    screen_y_middle = SCREEN_HEIGHT / 2

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(screen_x_middle, screen_y_middle)
    asteroid_field = AsteroidField()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        for entity in updatable:
            entity.update(dt)

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                raise SystemExit()
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000
   


if __name__ == "__main__":
    main()
