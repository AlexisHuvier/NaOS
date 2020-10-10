from naos.utils.utils import clamp

class Color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def darker(self, force=1):
        nb = clamp(force, 1)
        rgb = (clamp(x - 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def lighter(self, force=1):
        nb = clamp(force, 1)
        rgb = (clamp(x + 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def get_rgb(self):
        return self.r, self.g, self.b

    def get_rgba(self):
        return self.r, self.g, self.b, self.a

    def get_html(self):
        return ("#"+hex(self.r)[2:]+hex(self.g)[2:]+hex(self.b)[2:]+hex(self.a)[2:]).upper()

    def __repr__(self):
        return str(self.get_rgba())

    @classmethod
    def from_rgb(cls, r, g, b):
        color = Color()
        color.r = r
        color.g = g
        color.b = b
        return color

    @classmethod
    def from_rgba(cls, r, g, b, a):
        color = Color.from_rgb(r, g, b)
        color.a = a
        return color

    @classmethod
    def from_color(cls, color):
        return Color.from_rgba(*color.get_rgba())

    @classmethod
    def from_html(cls, html):
        if len(html) == 7 or len(html) == 9:
            if len(html) == 7:
                html += "FF"
            return Color.from_rgba(*(int(html[1:3], 16), int(html[3:5], 16), int(html[5:7], 16), int(html[7:9], 16)))
        else:
            raise ValueError("Hexa must be a 7 or 9 lenght string (#RRGGBBAA)")

    @classmethod
    def from_name(cls, name):
        colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GRAY": (128, 128, 128),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255),
            "FUCHSIA": (255, 0, 255),
            "YELLOW": (255, 255, 0),
            "CYAN": (0, 255, 255),
            "LIME": (0, 128, 0),
            "BROWN": (128, 0, 0),
            "NAVY_BLUE": (0, 0, 128),
            "OLIVE": (128, 128, 0),
            "PURPLE": (128, 0, 128),
            "TEAL": (0, 128, 128),
            "SILVER": (192, 192, 192),
            "ORANGE": (255, 128, 0)
        }
        return Color.from_rgb(*colors[name])
