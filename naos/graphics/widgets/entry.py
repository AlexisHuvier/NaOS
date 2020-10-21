import pygame
import string

from naos.graphics.widgets.widget import Widget
from naos.graphics.widgets.label import Label
from naos.utils import Font, clamp, Color

class Entry(Widget):
    def __init__(self, x, y, width=100, font=Font(color=Color.from_name("BLACK")),
        accepted="èàçù€ "+string.digits+string.ascii_letters+string.punctuation, image=None):
        super(Entry, self).__init__(x, y)

        self.width = width
        self.image = image
        self.label = Label(0, 0, "", font)
        self.text = ""
        self.focus = False
        self.accepted = accepted
        self.render = None
        self.update_render()
    
    def update_render(self):
        if self.label.text != self.text:
            self.label.text = self.text
            x = clamp(self.width - self.label.render.get_rect().width - 10, maxi=10)
            self.label.x = x
            self.label.y = self.render.get_rect().height / 2 - self.label.render.get_rect().height / 2
            self.label.update_render()

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.image, (self.width, 35))
        else:
            self.render = pygame.Surface((self.width, 35), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.width - 8, 27))
            white.fill((255, 255, 255))
            self.render.blit(white, (4, 4))
    
    def event(self, evt):
        if self.is_showed:
            if evt.type == pygame.KEYDOWN and self.focus:
                self.keypress(evt.key, evt.mod)
            elif evt.type == pygame.TEXTINPUT and self.focus:
                if evt.text in self.accepted:
                    self.text += evt.text
                    self.update_render()
            elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render.get_rect(x= self.get_real_x(), y= self.get_real_y()).collidepoint(*evt.pos):
                    self.focus = True
                else:
                    self.focus = False
                    self.update_render()

    def keypress(self, key, mod):
        mod -= 4096
        if key == pygame.K_BACKSPACE:
            if len(self.text):
                self.text = self.text[:-1]
                self.update_render()
    
    def show(self, screen):
        if self.is_showed:
            screen.blit(self.render, (self.x, self.y))
            self.label.show(self.render)
