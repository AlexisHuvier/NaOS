import pygame

from naos.utils import Color


class Window:
    def __init__(self, title, width, height, x = 100, y = 100):
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Arial", 15, 1)
        self.naos = None

    def event(self, evt):
        if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT and  pygame.Rect(self.x + self.width - 18, self.y+2, 16, 16).collidepoint(evt.pos[0], evt.pos[1]):
            self.naos.entities.remove(self)
            return True
        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y, self.width, 20))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(self.x, self.y+20, self.width, self.height))
        screen.blit(self.font.render(self.title, 0, Color.from_name("WHITE").get_rgba()), (self.x + 2, self.y + 2))
        pygame.draw.rect(screen, Color.from_name("RED").get_rgba(), pygame.Rect(self.x + self.width - 18, self.y+2, 16, 16))

    