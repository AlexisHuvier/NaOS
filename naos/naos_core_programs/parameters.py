import os

from naos.graphics.entities import Window
from naos.graphics.widgets import *
from naos.utils import Font

class Parameters(Window):
    def __init__(self, naos):
        super(Parameters, self).__init__("Paramètres", 400, 500)
        self.naos = naos
        self.add_widget(Label(150, 30, "Paramètres", Font(size=20)))
        self.add_widget(Label(150, 120, "Fond d'écran"))
        self.bg_entry = Entry(70, 150, width=260)
        self.add_widget(self.bg_entry)
        self.add_widget(Button(100, 400, "Valider", self.validate, size=(200, 50)))

        back = self.naos.db.executewithreturn("""SELECT background FROM parameters""")[0][0]
        if back is not None:
            self.bg_entry.text = back
            self.bg_entry.update_render()
    
    def validate(self):
        if self.naos.fs.exists(self.bg_entry.text):
            self.naos.set_background(self.bg_entry.text)

        self.close()



program = {
    "instance": Parameters,
    "infos": {
        "name": "Parameters",
        "author": "LavaPower"
    }
}