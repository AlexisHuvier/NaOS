import pygame

from naos.graphics.widgets.widget import Widget
from naos.utils import Color, clamp, Font

class ScrollPanel(Widget):
    def __init__(self, x, y, width, height, scroll_x = False, scroll_y = True):
        super(ScrollPanel, self).__init__(x, y)
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y
        self.width = width
        self.height = height
        self.font = Font()
        self.widgets = []
    
    def add_widget(self, widget):
        self.widgets.append(widget)
        widget.parent = self

    def event(self, evt):
        for i in self.widgets:
            if i.event(evt):
                return True
    
    def show(self, screen):
        if self.is_showed:
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y, self.width, self.height))
            if self.scroll_y:
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(4).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y, 20, self.height))
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y, 20, 20))
                screen.blit(self.font.render("^"), (self.x + self.width - 14, self.y + 5))
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y + self.height - 20, 20, 20))
                screen.blit(self.font.render("v"), (self.x + self.width - 14, self.y + self.height - 20))
            if self.scroll_x:
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(4).get_rgba(), pygame.Rect(self.x, self.y + self.height - 20, (self.width - 20) if self.scroll_y else self.width, 20))
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x, self.y + self.height - 20, 20, 20))
                screen.blit(self.font.render("<"), (self.x + 7, self.y + self.height - 17))
                pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x + ((self.width - 40) if self.scroll_y else (self.width - 20)), self.y + self.height - 20, 20, 20))
                screen.blit(self.font.render(">"), (self.x + ((self.width - 20) if self.scroll_y else self.width) - 13, self.y + self.height - 17))

            x = clamp(self.x, 0, self.width)
            y = clamp(self.y, 0, self.height)
            width = clamp(self.width, 0, self.width - x)
            height = clamp(self.height, 0, self.height - y)
            intra_canvas = screen.subsurface(pygame.Rect(x, y, width, height))
            for i in self.widgets:
                i.show(intra_canvas)