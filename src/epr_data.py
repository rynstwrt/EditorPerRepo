from os.path import expandvars
from constants import STORAGE_FILE
from pathlib import Path


class ErpData:
    def __init__(self):
        self.storage_file = Path()
        self.associations = []


    def save_associations(self):
        print(self.associations)


    def load_associations(self):
        print(self.associations)