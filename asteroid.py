import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        deflection_angle = random.uniform(20, 50)
        pos = self.velocity.rotate(deflection_angle)
        neg = self.velocity.rotate(-deflection_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, radius)
        ast2 = Asteroid(self.position.x, self.position.y, radius)

        ast1.velocity = pos * 1.2
        ast2.velocity = neg * 1.2
        
