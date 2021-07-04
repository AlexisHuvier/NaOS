import pygame

from naos.graphics.widgets.widget import Widget


class Image(Widget):
    def __init__(self, x, y, sprite, size=None, rotation=0, flipx=False, flipy=False):
        super(Image, self).__init__(x, y)

        self.sprite = sprite
        self.size = size
        self.rotation = rotation
        self.flipx = flipx
        self.flipy = flipy

        self.render = None
        self.update_render()
    
    def update_render(self):
        self.render = pygame.image.load(self.sprite).convert()
        if self.size is not None:
            self.render = pygame.transform.scale(self.render, self.size)
        if self.rotation != 0:
            self.render = pygame.transform.rotate(self.render, self.rotation)
        if self.flipx or self.flipy:
            self.render = pygame.transform.flip(self.render, self.flipx, self.flipy)
    
    def show(self, screen):
        if self.is_showed:
            screen.blit(self.render, (self.x, self.y))
