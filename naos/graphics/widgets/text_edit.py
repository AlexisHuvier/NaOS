import pygame
import string

from naos.graphics.widgets.widget import Widget
from naos.graphics.widgets.label import Label
from naos.utils import Font, Color


class TextEdit(Widget):
    def __init__(self, x, y, width=100, height=100, font=Font(color=Color.from_name("BLACK")),
                 accepted="èàçù€ "+string.digits+string.ascii_letters+string.punctuation, image=None):
        super(TextEdit, self).__init__(x, y)

        self.width = width
        self.height = height
        self.image = image
        self.label = Label(10, 10, "", font)
        self.text = ""
        self.focus = False
        self.accepted = accepted
        self.render = None
        self.update_render()
    
    def update_render(self):
        if self.label.text != self.text:
            self.label.text = self.text
            self.label.update_render()

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.render = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.width - 8, self.height - 8))
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
                if self.render.get_rect(x= self.get_real_x(), y=self.get_real_y()).collidepoint(*evt.pos):
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
        elif key == pygame.K_RETURN:
            self.text += "\n"
            print(self.text)
            self.update_render()
    
    def show(self, screen):
        if self.is_showed:
            screen.blit(self.render, (self.x, self.y))
            self.label.show(self.render)
