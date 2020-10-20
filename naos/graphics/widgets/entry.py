import pygame
import string

from naos.graphics.widgets.widget import Widget
from naos.utils import Font, clamp, Color

class Entry(Widget):
    def __init__(self, x, y, width=100, font=Font(color=Color.from_name("BLACK")),
        accepted="èàçù€ "+string.digits+string.ascii_letters+string.punctuation, image=None):
        super(Entry, self).__init__(x, y)

        self.width = width
        self.font = font
        self.image = image
        self.text = ""
        self.cursor = False
        self.focus = False
        self.cursortimer = 20
        self.accepted = accepted
        self.render = None
        self.update_render()
    
    def update_render(self):
        if self.cursor:
            text = self.font.render(self.text+"I")
        else:
            text = self.font.render(self.text)
        
        x = clamp(self.width - text.get_rect().width - 10, maxi=10)

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.image, (self.width, 35))
        else:
            self.render = pygame.Surface((self.width, 35), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.width - 8, 27))
            white.fill((255, 255, 255))
            self.render.blit(white, (4, 4))
        if len(self.text) or self.cursor:
            self.render.blit(text, (x, self.render.get_rect().height / 2 - text.get_rect().height / 2))
    
    def update(self):
        if self.is_showed and self.focus:
            if self.cursortimer <= 0:
                self.cursor = not self.cursor
                self.cursortimer = 20
                self.update_render()
            self.cursortimer -= 1
    
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
                    self.cursor = False
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
