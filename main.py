import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        for sprite in drawable:
            sprite.draw(screen)

        updateable.update(dt)
        pygame.display.flip()
        dt = FPS.tick(60) / 1000


if __name__ == "__main__":
    main()
