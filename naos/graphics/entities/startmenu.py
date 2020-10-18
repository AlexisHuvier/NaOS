import pygame

from naos.graphics.widgets import Button, Line
from naos.utils import Color

class StartMenu:
    def __init__(self, naos):
        self.open = False
        self.naos = naos
        self.x = 0
        self.y = self.naos.height - 202
        self.width = 300
        self.height = 202

        self.widgets = [
            Button(10, 10, "Programmes", self.open_program, size = (self.width - 20, 40)), 
            Button(10, 60, "Paramètres", size = (self.width - 20, 40)), 
            Line(0, 110, 300),
            Button(10, 120, "Eteindre", self.naos.stop, size=(self.width - 20, 40))
        ]
        for i in self.widgets:
            i.parent = self

    def get_real_y(self):
        return self.y

    def get_real_x(self):
        return self.x

    def open_program(self):
        self.open = False
        self.naos.open_window(self.naos.program_manager.get_program("Programmes").get_instance(self.naos))

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
