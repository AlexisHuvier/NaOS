import os

from naos.graphics.entities import Window
from naos.graphics.widgets import *

class ProgramLister(Window):
    def __init__(self, naos):
        super(ProgramLister, self).__init__("Programmes", 600, 300)
        self.naos = naos
        self.add_widget(Label(10, 10, "\n".join(self.naos.program_manager.get_programs_names())))

program = {
    "instance": ProgramLister,
    "infos": {
        "name": "Programmes",
        "author": "LavaPower"
    }
}