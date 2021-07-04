import pygame
import os
from datetime import datetime

from naos.utils import Color, Font


class NaOSBar:
    def __init__(self):
        self.logo = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "..", "files", "images", "logo.png")
        ).convert()
        self.logo = pygame.transform.scale(self.logo, (26, 26))
        self.naos = None
        self.font = Font(size=17, bold=True, color=Color.from_name("BLACK"))
        self.hour = self.font.render(datetime.now().strftime("%H:%M:%S"))

    def update(self):
        self.hour = self.font.render(datetime.now().strftime("%H:%M:%S"))

    def event(self, evt):
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.logo.get_rect(x=5, y=self.naos.height - 29).collidepoint(*evt.pos):
                self.naos.startmenu.open = not self.naos.startmenu.open
                return True
            
            for i, window in enumerate(self.naos.windows):
                if pygame.Rect(50+27*i, self.naos.height - 27, 20, 20).collidepoint(*evt.pos):
                    if window.open and window.focus:
                        self.naos.focus_window(None)
                        window.open = False
                    else:
                        self.naos.focus_window(window)
                        window.open = True                    
                    return True

        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(-1, self.naos.height - 33,
                                                                                  self.naos.width + 2, 34))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(0, self.naos.height - 32,
                                                                                 self.naos.width, 32))
        screen.blit(self.logo, (6, self.naos.height - 28))
        pygame.draw.line(screen, Color.from_name("BLACK").get_rgba(), (38, self.naos.height - 33),
                         (38, self.naos.height), 3)
        for i, window in enumerate(self.naos.windows):
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(3).get_rgba(), pygame.Rect(50+27*i,
                                                                                               self.naos.height - 27, 22, 22))
            screen.blit(
                self.font.render(window.title[0]),
                (50+27*i + (11 - self.font.rendered_size(window.title[0])[0] / 2),
                 self.naos.height - 27 + (11 - self.font.rendered_size(window.title[0])[1] / 2))
            )
        pygame.draw.line(screen, Color.from_name("BLACK").get_rgba(),
                         (self.naos.width - self.hour.get_rect().width - 10, self.naos.height - 33),
                         (self.naos.width - self.hour.get_rect().width - 10, self.naos.height), 3)
        screen.blit(self.hour, (self.naos.width - self.hour.get_rect().width - 5,
                                self.naos.height - 16 - self.hour.get_rect().height/2))