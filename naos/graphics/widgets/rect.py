import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Color


class Rect(Widget):
    def __init__(self, x, y, width, height, color=Color.from_name("BLACK")):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
    
    def show(self, screen):
        if self.is_showed:
            screen.fill(self.color.get_rgba(), pygame.Rect(self.x, self.y, self.width, self.height))
