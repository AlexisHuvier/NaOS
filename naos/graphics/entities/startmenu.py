import pygame

from naos.graphics.widgets import Button
from naos.utils import Color

class StartMenu:
    def __init__(self, naos):
        self.open = False
        self.naos = naos
        self.x = 0
        self.y = self.naos.height - 430
        self.width = 300
        self.height = 400

        self.widgets = [
            Button(10, 10, "Programmes", size = (self.width - 20, 40)), 
            Button(10, 60, "Paramètres", size = (self.width - 20, 40)), 
            Button(10, 110, "Eteindre", size = (self.width - 20, 40))
        ]
        for i in self.widgets:
            i.parent = self

    def event(self, evt):
        if self.open:
            for i in self.widgets:
                if i.event(evt):
                    return True
        return False

    def show(self, screen):
        if self.open:
            pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(self.x-1, self.y-1, self.width+2, self.height+2))
            pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(self.x, self.y, self.width, self.height))

            intra_canvas = screen.subsurface(pygame.Rect(self.x, self.y, self.width, self.height))
            for i in self.widgets:
                i.show(intra_canvas)
