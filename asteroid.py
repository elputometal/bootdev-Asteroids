import circleshape
import pygame
import constants
import logger
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            randomRotation = random.uniform(20,50)
            velocity1 = self.velocity.rotate(randomRotation)
            velocity2 = self.velocity.rotate(-randomRotation)
            newRadius = self.radius - constants.ASTEROID_MIN_RADIUS
            
            subAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            subAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)

            subAsteroid1.velocity = velocity1 * 1.2
            subAsteroid2.velocity = velocity2 * 1.2
