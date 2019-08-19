import os


class File:
    def __init__(self, path):
        self.path = path

    def file_path(self):
        if os.path.exists(self.path):
            return self.path
        raise FileNotFoundError("File dosen't exist")

    def read_file(self):
        with open(self.path, 'r') as file:
            return file.read().splitlines()
