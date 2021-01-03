import os

class FileSystem:
    def __init__(self, naos):
        self.naos = naos
    
    def exists(self, path):
        return os.path.exists(os.path.join(self.naos.paths["files"], path))
    
    def get_real_path(self, path):
        return os.path.join(self.naos.paths["files"], path)