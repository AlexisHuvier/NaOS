import os
from math import *

from naos.graphics.entities import Window
from naos.graphics.widgets import *
from naos.utils import Color

class Calculatrice(Window):
    def __init__(self, naos):
        super(Calculatrice, self).__init__("Calculatrice", 262, 300)
        self.naos = naos
        self.entry = Entry(10, 10, width=242)
        self.add_widget(self.entry)
        self.add_widget(Button(10, 50, "0", lambda x="0": self.add_text(x), size=(180, 40)))
        for i in range(1, 10):
            self.add_widget(Button(10+(i-1)%3*62, 100+(i-1)//3*50 , str(i), lambda x=str(i): self.add_text(x), size=(54, 40)))
        self.add_widget(Button(198, 50, "+", lambda x='+': self.add_text(x), size=(54, 40)))
        self.add_widget(Button(198, 100, "-", lambda x='-': self.add_text(x), size=(54, 40)))
        self.add_widget(Button(198, 150, "*", lambda x='*': self.add_text(x), size=(54, 40)))
        self.add_widget(Button(198, 200, "/", lambda x='/': self.add_text(x), size=(54, 40)))
        self.add_widget(Button(10, 250, "C", self.erase_text, size=(117, 40)))
        self.add_widget(Button(135, 250, "=", self.eval_text, size=(117, 40)))
    
    def add_text(self, text):
        self.entry.text += text
        self.entry.update_render()

    def erase_text(self):
        self.entry.text = ""
        self.entry.update_render()
    
    def eval_text(self):
        self.entry.text = str(eval(self.entry.text))
        self.entry.update_render()

program = {
    "instance": Calculatrice,
    "infos": {
        "name": "Calculatrice",
        "author": "LavaPower"
    }
}