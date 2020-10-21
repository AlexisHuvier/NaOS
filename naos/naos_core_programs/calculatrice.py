import os

from naos.graphics.entities import Window
from naos.graphics.widgets import *
from naos.utils import Color

class Calculatrice(Window):
    def __init__(self, naos):
        super(Calculatrice, self).__init__("Calculatrice", 200, 300)
        self.naos = naos
        self.add_widget(Rect(10, 10, 180, 40, Color.from_name("WHITE")))

program = {
    "instance": Calculatrice,
    "infos": {
        "name": "Calculatrice",
        "author": "LavaPower"
    }
}