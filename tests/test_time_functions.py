from work_schedule.work_schedule_data import DataWorkSchedule
from time_functions import (
    hours_range,
    time_interval,
    last_hour,
    first_hour,
    current_day_schedule,
    days,
    check_input_hour,
    days_dict
)


def test_hours_range_hour_in_range(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    result = hours_range(DataWorkSchedule(), 'Wednesday', '12')
    assert result is True


def test_hours_range_hour_out_of_range(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    result = hours_range(DataWorkSchedule(), 'Friday', '7')
    assert result is False


def test_time_interval(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    max_number = time_interval('Tuesday', DataWorkSchedule(), 14)
    assert max_number == 5


def test_another_time_interval(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    max_number = time_interval('Thursday', DataWorkSchedule(), 11)
    assert max_number == 7


def test_last_hour(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    last_h = last_hour(DataWorkSchedule(), 'Monday')
    assert last_h == '17'


def test_first_hour(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    first_h = first_hour(DataWorkSchedule(), 'Sunday')
    assert first_h == '8'


def test_current_day_schedule(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    schedule = current_day_schedule(DataWorkSchedule(), 'Friday')
    assert schedule == 'Friday open 8 - 22'


def test_days():
    day_value_dict, value_day_dict = days()
    assert day_value_dict == {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5,
        'Sunday': 6}
    assert value_day_dict == {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday',
        6: 'Sunday'}


def test_check_input_hour_correct_inp():
    inp = check_input_hour('12')
    assert inp is True


def test_check_input_hour_wrong_inp():
    inp = check_input_hour('123')
    assert inp is False


def test_check_input_hour_wrong_number():
    inp = check_input_hour('s1')
    assert inp is False


def test_check_input_hour_empty():
    inp = check_input_hour('')
    assert inp is False


def test_days_dict():
    day = days_dict('7')
    assert day == 'Sunday'
