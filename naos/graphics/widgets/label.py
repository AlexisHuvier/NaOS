import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Font

class Label(Widget):
    def __init__(self, x, y, text, font=Font(size=16), background=None):
        super().__init__(x, y)
        self.text = text
        self.font = font
        self.background = background
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
                if self.background is not None:
                    screen.fill(self.background.get_rgba(), self.render.get_rect())
                screen.blit(self.render, (self.x, self.y))
            else:
                for i, render in enumerate(self.renders):
                    if self.background is not None:
                        screen.fill(self.background.get_rgba(), render.get_rect())
                    screen.blit(render, (self.x, self.y + 20 + render.get_rect().width * i + 2))