import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y - y
        self.radius = radius
        
    def draw(self, screen):
        asteroid_sprite = self.Asteroid()
        pygame.draw.circle(screen, "white", asteroid_sprite, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
