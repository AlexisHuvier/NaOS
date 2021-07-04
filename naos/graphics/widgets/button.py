import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Font, Color


class Button(Widget):
    def __init__(self, x, y, text, command=None, font=Font(), size=(100, 40),
                 background=Color.from_name("GRAY").darker(5)):
        super().__init__(x, y)
        self.text = text
        self.command = command
        self.font = font
        self.background = background
        self.size = size
        self.is_hover = False
        self.update_render()

    def update_render(self):
        if isinstance(self.background, Color):
            self.render = pygame.Surface(self.size, pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill(self.background.get_rgba())
        else:
            self.render = pygame.image.load(self.background).convert()
            self.render = pygame.transform.scale(self.render, self.size)

        text_render = self.font.render(self.text)
        x = self.size[0] - self.render.get_rect().width / 2 - text_render.get_rect().width / 2
        y = self.size[1] - self.render.get_rect().height / 2 - text_render.get_rect().height / 2
        self.render.blit(text_render, (x, y))
    
    def show(self, screen):
        if self.is_showed:
            screen.blit(self.render, (self.x, self.y))

    def event(self, evt):
        if self.is_showed:
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render.get_rect(x=self.get_real_x(), y=self.get_real_y()).collidepoint(*evt.pos) and \
                        self.command is not None:
                    self.command()
                    return True                
        return False
