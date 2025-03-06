from os.path import expandvars
from constants import STORAGE_FILE
from pathlib import Path


class EprData:
    def __init__(self, util):
        self._util = util
        self._storage_file_path = Path()
        self._associations = []


    def set_associations(self, association_list):
        print(f"Setting association list to {association_list}!")
        self._associations = association_list


    def get_associations(self):
        return self._associations


    def save_associations(self):
        print("Saving association list!")
        print(self._associations)


    def load_associations(self):
        print("Loading association list!")
        print(self._associations)