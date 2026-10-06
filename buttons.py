import pygame
from constants import *
#acts as a way to start/restart the game
class Button():
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        
        # Render text surface once to save performance
        self.text_surf = font.render(text, True, COLOR_WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
    
    def draw(self, surface):
        button = font.render("Start", True, (255, 255, 255))
        
