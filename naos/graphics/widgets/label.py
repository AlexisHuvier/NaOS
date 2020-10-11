import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Font

class Label(Widget):
    def __init__(self, x, y, text, font=Font()):
        super().__init__(x, y)
        self.text = text
        self.font = font
        self.render = self.font.render(self.text)
    
    def update_render(self):
        self.render = self.font.render(self.text)
    
    def show(self, screen):
        if self.is_showed:
            screen.blit(self.render, (self.x + self.parent.x, self.y + self.parent.y + 20))