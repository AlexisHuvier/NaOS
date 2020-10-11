import pygame

from naos.utils import Color

class StartMenu:
    def __init__(self):
        self.open = False
        self.naos = None

    def event(self, evt):
        return False

    def show(self, screen):
        if self.open:
            pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(-1, 649, 302, 402))
            pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(0, 650, 300, 400))