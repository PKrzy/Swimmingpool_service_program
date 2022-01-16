from attributes.name_tracks_data import Attributes, load_data


def test_load_data():
    name, tracks = load_data('tests/test_attributes.txt')
    assert name == 'Neptun'
    assert tracks == '10'


def test_attributes_path():
    path = Attributes().attributes_path()
    assert path == 'attributes/swimmingpool_attributes.txt'


def test_name(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)
    assert Attributes().name() == 'Neptun'


def test_tracks_number(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)
    assert Attributes().tracks() == 10


def test_change_name(monkeypatch):
    def fake_path(d):
        return 'tests/test_change_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)
    Attributes().change_name('Orca')
    assert Attributes().name() == 'Orca'


def test_change_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_change_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)
    Attributes().change_tracks('5')
    assert Attributes().tracks() == 5
