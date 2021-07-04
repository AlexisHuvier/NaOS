import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Color


class Line(Widget):
    def __init__(self, x, y, xlength=0, ylength=0, width=2, color=Color.from_name("BLACK")):
        super().__init__(x, y)
        self.endx = x + xlength
        self.endy = y + ylength
        self.width = width
        self.color = color
    
    def show(self, screen):
        if self.is_showed:
            pygame.draw.line(screen, self.color.get_rgba(), (self.x, self.y), (self.endx, self.endy))
