"""Load files with swimmingpool attributes"""


def load_data(path):
    file = open(path, 'r')
    line = file.readline()
    line = line.rstrip()
    tokens = line.split(',')
    name, tracks_num = tokens
    return name, tracks_num


class Attributes():

    """Split attributes"""

    def __init__(self):
        self._attributes_path = 'attributes/swimmingpool_attributes.txt'
        self._name = load_data(self.attributes_path())[0]
        self._tracks = int(load_data(self.attributes_path())[1])

    def name(self):
        return self._name

    def attributes_path(self):
        return self._attributes_path

    def tracks(self):
        return self._tracks

    """Change name and save it in file"""

    def change_name(self, new_name):
        tracks = self.tracks()
        open(self.attributes_path(), 'w').close()
        file = open(self.attributes_path(), 'a')
        file.write(f'{new_name},{tracks}')

    """change number of tracks and save it in file"""

    def change_tracks(self, new_tracks_number):
        name = self.name()
        open(self.attributes_path(), 'w').close()
        file = open(self.attributes_path(), 'a')
        file.write(f'{name},{new_tracks_number}')
