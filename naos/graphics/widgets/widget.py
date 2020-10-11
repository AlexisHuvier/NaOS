class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_showed = True
        self.parent = None

    def update(self):
        pass

    def event(self, evt):
        return False

    def show(self, screen):
        pass