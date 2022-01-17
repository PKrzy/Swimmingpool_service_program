from swimmingpool import Swimmingpool
from attributes.name_tracks_data import Attributes
from work_schedule.work_schedule_data import DataWorkSchedule
from swimmingpool import (
    check_current_day_hours,
    check_next_day_hours,
    check_next_day,
    check_current_hours_add_tracks,
    check_next_day_hours_and_tracks,
    check_next_day_sw_school
)


def test_swimmingpool_name(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    assert pool.name() == 'Neptun'


def test_swimmingpool_new_name(monkeypatch):
    def fake_path(d):
        return 'tests/test_change_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    pool.set_name('Orca')
    assert pool.name() == 'Orca'


def test_swimmingpool_attributes():
    pool = Swimmingpool()
    assert isinstance(pool.attributes(), Attributes) is True


def test_tracks_number(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    assert pool.tracks_number() == 10


def test_set_tracks_number(monkeypatch):
    def fake_path(d):
        return 'tests/test_change_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    pool.set_tracks_number(5)
    assert pool.tracks_number() == 5


def test_sw_work_schedule(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    pool = Swimmingpool()
    assert pool.work_schedule() == {
        "Monday": {
            "12": [0, 0], "13": [0, 0], "14": [0, 0],
            "15": [0, 0], "16": [0, 0], "17": [0, 0]
        },
        "Tuesday": {
            "11": [0, 0], "12": [0, 0], "13": [0, 0], "14": [0, 0],
            "15": [0, 0], "16": [0, 0], "17": [0, 0], "18": [0, 0]
            },
        "Wednesday": {
            "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0],
            "12": [0, 0], "13": [0, 0], "14": [0, 0], "15": [0, 0],
            "16": [0, 0], "17": [0, 0]
            },
        "Thursday": {
            "10": [0, 0], "11": [0, 0], "12": [0, 0], "13": [0, 0],
            "14": [0, 0], "15": [0, 0], "16": [0, 0], "17": [0, 0]
            },
        "Friday": {
            "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0],
            "12": [0, 0], "13": [0, 0], "14": [0, 0], "15": [0, 0],
            "16": [0, 0], "17": [0, 0], "18": [0, 0], "19": [0, 0],
            "20": [0, 0], "21": [0, 0]
            },
        "Saturday": {
            "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0],
            "12": [0, 0], "13": [0, 0], "14": [0, 0], "15": [0, 0],
            "16": [0, 0], "17": [0, 0], "18": [0, 0], "19": [0, 0],
            "20": [0, 0], "21": [0, 0]
            },
        "Sunday": {
            "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0],
            "12": [0, 0], "13": [0, 0], "14": [0, 0], "15": [0, 0],
            "16": [0, 0], "17": [0, 0], "18": [0, 0], "19": [0, 0]}}


def test_space(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    assert pool.space() == 50


def test_data():
    pool = Swimmingpool()
    assert isinstance(pool.data(), DataWorkSchedule) is True


def test_max_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_path)

    pool = Swimmingpool()
    assert pool.max_tracks() == 3


def test_check_seat(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    pool = Swimmingpool()
    assert pool.check_seat('12', '4', 'Monday', 5) is None


def test_check_seat_no_space(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    assert pool.check_seat('8', '2', 'Sunday', 5) is False


def test_check_seat_and_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    assert pool.check_seat_and_tracks('11', '2', 'Sunday', 2) is None


def test_check_seat_and_tracks_no_space(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    assert pool.check_seat_and_tracks('15', '1', 'Saturday', 2) is False


def test_check_seat_and_tracks_no_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    assert pool.check_seat_and_tracks('20', '1', 'Friday', 2) is False


def test_check_free_term(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    term = pool.check_free_term('8', '2', 'Sunday', 5)
    assert term == 'Next free term Sunday 10'


def test_check_free_term_another_day(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    term = pool.check_free_term('18', '2', 'Sunday', 11)
    assert term == 'Next free term Monday 12'


def test_check_free_term_swimming_school(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    term = pool.check_free_term_swimming_school('16', '1', 'Monday', 2)
    assert term == 'Next free term Monday 17'


def test_check_free_term_swimming_school_another_day(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    term = pool.check_free_term_swimming_school('16', '3', 'Monday', 2)
    assert term == 'Next free term Tuesday 15'


def test_add_person(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    pool = Swimmingpool()
    pool.add_person('12', '2', 'Monday', 5)
    assert pool.work_schedule()['Monday']['12'] == [5, 0]
    assert pool.work_schedule()['Monday']['13'] == [5, 0]
    DataWorkSchedule().clear_day('Monday')


def test_add_swimming_school(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    pool = Swimmingpool()
    pool.add_swimming_school('15', '3', 'Tuesday', 2)
    assert pool.work_schedule()['Tuesday']['15'] == [10, 2]
    assert pool.work_schedule()['Tuesday']['16'] == [10, 2]
    assert pool.work_schedule()['Tuesday']['17'] == [10, 2]
    DataWorkSchedule().clear_day('Tuesday')


def test_check_current_day_hours(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    hours_dict = pool.work_schedule()['Tuesday']
    space = pool.space()
    data = DataWorkSchedule()
    free_positions, free_hour = check_current_day_hours(
        14, 2, hours_dict,
        2, space, data, 'Tuesday')
    assert free_positions == 2
    assert free_hour == '15'


def test_check_next_day_hours(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    hours_dict = pool.work_schedule()['Wednesday']
    space = pool.space()
    free_hour, free_positions = check_next_day_hours(
        0, '', 2,
        '8', '17', hours_dict, 2, space)
    assert free_positions == 2
    assert free_hour == '8'


def test_check_next_day(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    data = DataWorkSchedule()
    work_schedule = pool.work_schedule()
    space = pool.space()
    free_hour, free_positions, next_day = check_next_day(
        0, '', 2, 'Sunday',
        data, work_schedule, 5, space)
    assert free_hour == '12'
    assert free_positions == 2
    assert next_day == 'Monday'


def test_current_hours_add_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    data = DataWorkSchedule()
    max_tracks = pool.max_tracks()
    space = pool.space()
    hours_dict = pool.work_schedule()['Wednesday']
    free_positions, free_hour = check_current_hours_add_tracks(
        10, 4, hours_dict,
        5, 1, space, data,
        'Wednesday', max_tracks)
    assert free_positions == 4
    assert free_hour == '10'


def test_check_next_day_hours_and_tracks(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    hours_dict = pool.work_schedule()['Wednesday']
    max_tracks = pool.max_tracks()
    space = pool.space()
    free_hour, free_positions = check_next_day_hours_and_tracks(
        0, '', 3,
        '8', '17', hours_dict,
        5, space, 1, max_tracks)
    assert free_hour == '8'
    assert free_positions == 3


def test_check_next_day_sw_school(monkeypatch):
    def fake_path(d):
        return 'tests/test_sw_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)

    def fake_attributes(e):
        return 'tests/test_attributes.txt'
    monkeypatch.setattr(Attributes, 'attributes_path', fake_attributes)

    pool = Swimmingpool()
    data = DataWorkSchedule()
    work_schedule = pool.work_schedule()
    space = pool.space()
    max_tracks = pool.max_tracks()
    free_hour, free_positions, next_day = check_next_day_sw_school(
        0, '', 5,
        'Friday', data, work_schedule, 5,
        space, 1, max_tracks)
    assert free_hour == '8'
    assert free_positions == 5
    assert next_day == 'Saturday'
