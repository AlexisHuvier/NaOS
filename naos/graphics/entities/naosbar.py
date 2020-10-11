import pygame
import os

from naos.utils import Color

class NaOSBar:
    def __init__(self):
        self.logo = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "..", "files", "images", "logo.png")).convert()
        self.logo = pygame.transform.scale(self.logo, (20, 20))

    def event(self, evt):
        if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT and self.logo.get_rect(x=5, y=1055).collidepoint(evt.pos[0], evt.pos[1]):
            print("CLICK")
            return True
        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(-1, 1049, 1922, 32))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(0, 1050, 1920, 30))
        screen.blit(self.logo, (5, 1055))