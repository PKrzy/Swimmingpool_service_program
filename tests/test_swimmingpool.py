from io import StringIO
from swimmingpool import Swimmingpool
from attributes.name_tracks_data import Attributes


def test_swimmingpool_name(monkeypatch):
    def pool_name(d):
        return 'Neptun'
    monkeypatch.setattr(Attributes, 'name', pool_name)
    pool = Swimmingpool()
    assert pool.name() == 'Neptun'


def test_swimmingpool_new_name(monkeypatch):
    fake_file = StringIO('Neptun, 12')
    monkeypatch.setattr(Attributes, 'name', pool_name)
    pool = Swimmingpool()
    assert pool.name() == 'Neptun'
    assert pool.set_name('Orca') == 'Orca'