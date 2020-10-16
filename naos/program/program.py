class Program:
    def __init__(self, module):
        self.module = module
        self.program_info = self.module.program

    def get_instance(self, naos):
        return self.program_info["instance"](naos)
    
    def get_program_info(self):
        return self.program_info["infos"]