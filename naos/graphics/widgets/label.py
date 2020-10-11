import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Font

class Label(Widget):
    def __init__(self, x, y, text, font=Font(size=16)):
        super().__init__(x, y)
        self.text = text
        self.font = font
        self.update_render()
    
    def update_render(self):
        if "\n" in self.text:
            self.renders = [self.font.render(i) for i in self.text.split("\n")]
            self.single = False
        else:
            self.render = self.font.render(self.text)
            self.single = True
    
    def show(self, screen):
        if self.is_showed:
            if self.single:
                screen.blit(self.render, (self.x, self.y))
            else:
                for i in range(len(self.renders)):
                    screen.blit(self.renders[i], (self.x, self.y + 20 + (self.font.rendered_size(self.text.split("\n")[i])[1] * i + 2)))