import json


def get_path_attributes():
    with open("config.json", 'r') as fh:
        path = json.load(fh)["attributes_path"]
    return path


def load_data(path):
    """Load files with swimmingpool attributes"""

    file = open(path, 'r')
    line = file.readline()
    line = line.rstrip()
    tokens = line.split(',')
    name, tracks_num = tokens
    return name, tracks_num


class Attributes():

    def __init__(self):
        """Split attributes"""

        self._attributes_path = get_path_attributes()
        self._name = load_data(self.attributes_path())[0]
        self._tracks = int(load_data(self.attributes_path())[1])

    def name(self):
        return self._name

    def attributes_path(self):
        return self._attributes_path

    def tracks(self):
        return self._tracks

    def change_name(self, new_name):
        """Change name and save it in file"""

        tracks = self.tracks()
        open(self.attributes_path(), 'w').close()
        file = open(self.attributes_path(), 'a')
        file.write(f'{new_name},{tracks}')

    def change_tracks(self, new_tracks_number):
        """change number of tracks and save it in file"""

        name = self.name()
        open(self.attributes_path(), 'w').close()
        file = open(self.attributes_path(), 'a')
        file.write(f'{name},{new_tracks_number}')
