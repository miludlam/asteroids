# this allows us to use code from the open-source pygame
# library throughout this file
import pygame
# import from local modules
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    # initialize pygame and set screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # initialize object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # initialize a new clock object and delta time variable
    clock = pygame.time.Clock()
    dt = 0

    # initialize Player obj in center of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for obj in updatable:
            obj.update(dt)
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


