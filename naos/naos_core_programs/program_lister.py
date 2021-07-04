from naos.graphics.entities import Window
from naos.graphics.widgets import *


class ProgramLister(Window):
    def __init__(self, naos):
        super(ProgramLister, self).__init__("Programmes", 600, 300)
        self.naos = naos
        scrollpanel = ScrollPanel(10, 10, 580, 280)
        for k, v in enumerate(self.naos.program_manager.get_programs_names()):
            scrollpanel.add_widget(Button(10, 10+(k*50), v, lambda v=v: self.open_program(v), size=(540, 40)))
        self.add_widget(scrollpanel)

    def open_program(self, v):
        self.naos.open_window(self.naos.program_manager.get_program(v).get_instance(self.naos))


program = {
    "instance": ProgramLister,
    "infos": {
        "name": "Programmes",
        "author": "LavaPower"
    }
}
