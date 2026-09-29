import pygame
from constants import *
class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.numb = 0
        self.timer = 0
    
    def hit(self, other):
        if other.radius <= ASTEROID_MIN_RADIUS:
            self.numb += POINTS_PER_HIT * 2
            return
        self.numb += POINTS_PER_HIT

    def update(self, dt: float) -> None:
        self.timer += 1 * dt
     
    def printout(self):
        round_timer = round(self.timer)
        print("Game over!")
        print("==================")
        print(f"time {round_timer} sconds")
        print(f"Score {self.numb + (round_timer * 10)} pts")
        print("==================")
