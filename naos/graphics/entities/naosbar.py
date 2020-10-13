import pygame
import os

from naos.utils import Color, Font

class NaOSBar:
    def __init__(self):
        self.logo = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "..", "files", "images", "logo.png")).convert()
        self.logo = pygame.transform.scale(self.logo, (20, 20))
        self.naos = None
        self.font = Font(bold=True)

    def event(self, evt):
        if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT:
            if self.logo.get_rect(x=5, y=1055).collidepoint(evt.pos[0], evt.pos[1]):
                self.naos.startmenu.open = not self.naos.startmenu.open
                return True
            
            for i, window in enumerate(self.naos.windows):
                if pygame.Rect(40+25*i, 1055, 20, 20).collidepoint(evt.pos[0], evt.pos[1]):
                    window.open = not window.open
                    return True

        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(-1, 1049, 1922, 32))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(0, 1050, 1920, 30))
        screen.blit(self.logo, (5, 1055))
        pygame.draw.line(screen, Color.from_name("BLACK").get_rgba(), (30, 1049), (30, 1080), 3)
        for i, window in enumerate(self.naos.windows):
            pygame.draw.rect(screen, Color.from_name("GRAY").lighter(2).get_rgba(), pygame.Rect(40+25*i, 1055, 20, 20))
            screen.blit(self.font.render(window.title[0]), (40+25*i + (10 - self.font.rendered_size(window.title[0])[0] / 2), 1055 + (10 - self.font.rendered_size(window.title[0])[1] / 2)))

