import pygame

from naos.utils import Color, Font


class Window:
    def __init__(self, title, width, height, x = 100, y = 100):
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font = Font(bold=True)
        self.naos = None
        self.is_dragged = False
        self.drag_offset = [0, 0]

    def event(self, evt):
        if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT and  pygame.Rect(self.x + self.width - 18, self.y+2, 16, 16).collidepoint(evt.pos[0], evt.pos[1]):
            self.naos.entities.remove(self)
            return True
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT and pygame.Rect(self.x, self.y, self.width, 20).collidepoint(evt.pos[0], evt.pos[1]):
            self.is_dragged = True
            self.drag_offset = [evt.pos[0] - self.x, evt.pos[1] - self.y]
            return True
        if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT and self.is_dragged:
            self.is_dragged = False
            self.drag_offset = [0, 0]
            return True
        if evt.type == pygame.MOUSEMOTION and self.is_dragged:
            self.x = evt.pos[0] - self.drag_offset[0]
            self.y = evt.pos[1] - self.drag_offset[1]
            return True

        return False

    def show(self, screen):
        pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(self.x-1, self.y-1, self.width + 2, self.height + 22))
        pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y, self.width, 20))
        pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(self.x, self.y+20, self.width, self.height))
        screen.blit(self.font.render(self.title), (self.x + 2, self.y + 2))
        pygame.draw.rect(screen, Color.from_name("RED").get_rgba(), pygame.Rect(self.x + self.width - 18, self.y+2, 16, 16))

    