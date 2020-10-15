import pygame

from naos.utils import Color, Font, clamp


class Window:
    def __init__(self, title, width, height, x = 100, y = 100):
        self.title = title
        self.width = clamp(width, 60)
        self.height = clamp(height, 10)
        self.x = clamp(x, 0, 1920)
        self.y = clamp(y+20, 0, 1080)
        self.font = Font(bold=True)
        self.naos = None
        self.is_dragged = False
        self.drag_offset = [0, 0]
        self.widgets = []
        self.focus = False
        self.open = True

    def add_widget(self, widget):
        if widget.parent is None:
            self.widgets.append(widget)
            widget.parent = self
        
    def update(self):
        for i in self.widgets:
            i.update()

    def close(self):
        self.naos.windows.remove(self)

    def event(self, evt):
        if self.open:
            if evt.type == pygame.MOUSEBUTTONUP and evt.button == pygame.BUTTON_LEFT:
                if self.is_dragged:
                    self.is_dragged = False
                    self.drag_offset = [0, 0]
                if pygame.Rect(self.x + self.width - 18, self.y - 18, 16, 16).collidepoint(*evt.pos):
                    self.close()
                if pygame.Rect(self.x + self.width - 36, self.y - 18, 16, 16).collidepoint(*evt.pos):
                    self.open = not self.open

            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT and pygame.Rect(self.x, self.y - 20, self.width, 20).collidepoint(*evt.pos):
                self.is_dragged = True
                self.drag_offset = [evt.pos[0] - self.x, evt.pos[1] - self.y]
                return True
            if evt.type == pygame.MOUSEMOTION and self.is_dragged:
                self.x = evt.pos[0] - self.drag_offset[0]
                self.y = evt.pos[1] - self.drag_offset[1]

            if self.focus:
                for i in self.widgets:
                    if i.event(evt):
                        return True
            
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT and pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(*evt.pos):
                return True

        return False

    def show(self, screen):
        if self.open:
            pygame.draw.rect(screen, Color.from_name("BLACK").get_rgba(), pygame.Rect(self.x-1, self.y-21, self.width + 2, self.height + 22))
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(2).get_rgba(), pygame.Rect(self.x, self.y-20, self.width, 20))
            pygame.draw.rect(screen, Color.from_name("GRAY").get_rgba(), pygame.Rect(self.x, self.y, self.width, self.height))

            temp = self.title
            while temp != "..." and self.font.rendered_size(temp)[0] > self.width - 44:
                temp = temp[:-1] if temp == self.title else temp[:-4] + "..."
            screen.blit(self.font.render(temp), (self.x + 4, self.y - 18))
            pygame.draw.rect(screen, Color.from_name("GRAY").darker(5).get_rgba(), pygame.Rect(self.x + self.width - 36, self.y - 18, 16, 16))
            pygame.draw.line(screen, Color.from_name("BLACK").get_rgba(), (self.x + self.width - 32, self.y - 11), (self.x + self.width - 24, self.y - 11), 2)
            pygame.draw.rect(screen, Color.from_name("RED").get_rgba(), pygame.Rect(self.x + self.width - 18, self.y - 18, 16, 16))

            x = clamp(self.x, 0, self.naos.width)
            y = clamp(self.y, 0, self.naos.height)
            width = clamp(self.width, 0, self.naos.width - x)
            height = clamp(self.height, 0, self.naos.height - y)
            intra_canvas = screen.subsurface(pygame.Rect(x, y, width, height))
            for i in self.widgets:
                i.show(intra_canvas)

    