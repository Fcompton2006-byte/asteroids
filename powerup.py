import pygame
from asteroids import Asteroid
from constants import *

class Powerups(Asteroid):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "blue", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
         self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        