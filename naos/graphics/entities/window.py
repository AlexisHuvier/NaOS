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

    def event(self, evt):
        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y, self.width, 20))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(self.x, self.y+20, self.width, self.height))
        screen.blit(self.font.render(self.title, 0, Color.from_name("WHITE").get_rgba()), (self.x + 2, self.y + 2))

    