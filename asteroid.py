import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None: 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        first_asteroid_angle = self.velocity.rotate(rand_angle)
        second_asteroid_angle = self.velocity.rotate(rand_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position, self.position, new_asteroid_radius)
        ast_2 = Asteroid(self.position, self.position, new_asteroid_radius)
        ast_1.velocity = first_asteroid_angle * 1.2
        ast_2.velocity = second_asteroid_angle * 1.2



