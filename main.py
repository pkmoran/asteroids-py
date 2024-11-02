import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.is_colliding_with(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()