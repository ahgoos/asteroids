import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-1 * angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1, a2 = (
            Asteroid(self.position.x, self.position.y, new_radius),
            Asteroid(self.position.x, self.position.y, new_radius),
        )
        a1.velocity, a2.velocity = v1 * 1.2, v2 * 1.2
