class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_showed = True
        self.parent = None

    def get_real_y(self):
        if self.parent is None:
            return self.y
        else:
            return self.parent.get_real_y() + self.y
        
    def get_real_x(self):
        if self.parent is None:
            return self.x
        else:
            return self.parent.get_real_x() + self.x

    def update(self):
        pass

    def event(self, evt):
        return False

    def show(self, screen):
        pass
