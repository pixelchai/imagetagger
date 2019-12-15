from providers import Provider
import os

class FolderProvider(Provider):
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.files = os.listdir(self.path)
        self.cur_index = 0

    def get_next(self):
        try:
            return os.path.join(self.path, self.files[self.cur_index])
        finally:
            self.cur_index += 1
