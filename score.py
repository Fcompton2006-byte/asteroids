import pygame
from constants import*
class Score():
    def __init__(self):
        self.numb = 0
    
    def hit(self, other):
        if other.radius <= ASTEROID_MIN_RADIUS:
            self.numb += POINTS_PER_HIT * 2
            return
        self.numb += POINTS_PER_HIT
    
     