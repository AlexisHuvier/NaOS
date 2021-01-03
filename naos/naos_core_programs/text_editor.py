import os

from naos.graphics.entities import Window
from naos.graphics.widgets import *
from naos.utils import Color

class TextEditor(Window):
    def __init__(self, naos):
        super(TextEditor, self).__init__("Editeur de texte", 500, 300)
        self.naos = naos
        self.add_widget(TextEdit(10, 10, 480, 280))
        

program = {
    "instance": TextEditor,
    "infos": {
        "name": "Editeur de texte",
        "author": "LavaPower"
    }
}