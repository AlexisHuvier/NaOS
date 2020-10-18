import pygame

from naos.graphics.widgets.widget import Widget
from naos.graphics.widgets.button import Button
from naos.graphics.widgets.label import Label
from naos.utils import Color, clamp, Font

class ScrollPanel(Widget):
    def __init__(self, x, y, width, height):
        super(ScrollPanel, self).__init__(x, y)
        self.width = width
        self.height = height
        self.font = Font()
        self.widgets = []
        self.bornes = [0, 0]
        
    def add_widget(self, widget):
        self.widgets.append(widget)
        widget.parent = self
        if len(self.widgets) == 0:
            self.bornes[0] = widget.y
        if isinstance(widget, Button):
            self.bornes[1] = widget.y + widget.size[1]
        elif isinstance(widget, Label):
            self.bornes[1] = widget.y + widget.font.rendered_size(widget.text)[1]

    def event(self, evt):
        if self.is_showed:
            if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT:
                if pygame.Rect(self.get_real_x() + self.width - 20, self.get_real_y(), 20, 20).collidepoint(*evt.pos):
                    if self.widgets[0].y <= -self.bornes[0]:
                        for i in self.widgets:
                            i.y += 10
                    return True
                if pygame.Rect(self.get_real_x() + self.width - 20, self.get_real_y() + self.height - 20, 20, 20).collidepoint(*evt.pos):
                    if self.widgets[0].y >= -self.bornes[1] + self.height:
                        for i in self.widgets:
                            i.y -= 10
                    return True
            for i in self.widgets:
                if i.event(evt):
                    return True
        return False
    
    def show(self, screen):
        if self.is_showed:
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(4).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y, 20, self.height))
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y, 20, 20))
            screen.blit(self.font.render("^"), (self.x + self.width - 14, self.y + 5))
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(6).get_rgba(), pygame.Rect(self.x + self.width - 20, self.y + self.height - 20, 20, 20))
            screen.blit(self.font.render("v"), (self.x + self.width - 14, self.y + self.height - 20))

            x = clamp(self.x, 0, self.width)
            y = clamp(self.y, 0, self.height)
            width = clamp(self.width, 0, self.width - x)
            height = clamp(self.height, 0, self.height - y)
            intra_canvas = screen.subsurface(pygame.Rect(x, y, width, height))
            for i in self.widgets:
                i.show(intra_canvas)