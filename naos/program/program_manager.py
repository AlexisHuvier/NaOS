import os
import importlib

from naos.program.program import Program


class ProgramManager:
    def __init__(self):
        self.programs = []
        self.load_programs()
    
    def load_programs(self):
        for i in os.listdir(os.path.join(os.path.dirname(__file__), "..", "naos_core_programs")):
            name = ".".join(i.split(".")[:-1])
            if name != "__init__" and name != "":
                self.programs.append(Program(importlib.import_module("naos.naos_core_programs."+name)))

    def get_program(self, name):
        for i in self.programs:
            if i.get_program_info()["name"] == name:
                return i
    
    def get_programs_names(self):
        return [i.get_program_info()["name"] for i in self.programs]
