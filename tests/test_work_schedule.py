from work_schedule.work_schedule_data import DataWorkSchedule, \
    load_work_schedule
import json


def test_load_work_schedule():
    work_dict = load_work_schedule('tests/test_work_schedule.txt')
    assert work_dict == {
        'Monday': (12, 18), 'Tuesday': (11, 19),
        'Wednesday': (8, 18), 'Thursday': (10, 18),
        'Friday': (8, 22), 'Saturday': (8, 22), 'Sunday': (8, 20)}


def test_work_schedule_path():
    path = DataWorkSchedule().ws_path()
    assert path == 'work_schedule/work_schedule.json'


def test_work_schedule_data(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    data = DataWorkSchedule().data()
    assert data == {
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


def test_save_data(monkeypatch):
    def fake_path(d):
        return 'tests/test_save_file_ws.json'
    data = {"Monday": {
        "12": [0, 0], "13": [0, 0], "14": [0, 0]},
        "Tuesday": {
        "11": [0, 0], "12": [0, 0], "13": [0, 0]}
    }
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    DataWorkSchedule().save_data(data)
    fp = open('tests/test_save_file_ws.json', 'r')
    test_data = json.load(fp)
    assert test_data == data


def test_load_new_work_schedule(monkeypatch):
    def fake_path(d):
        return 'tests/test_new_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    path = 'tests/test_work_schedule.txt'
    DataWorkSchedule().load_new_work_schedule(path)
    fp = open('tests/test_new_work_schedule.json', 'r')
    test_data = json.load(fp)
    fh = open('tests/test_work_schedule.json', 'r')
    expected_data = json.load(fh)
    assert test_data == expected_data


def test_clear_day(monkeypatch):
    def fake_path(d):
        return 'tests/test_work_schedule.json'
    monkeypatch.setattr(DataWorkSchedule, 'ws_path', fake_path)
    DataWorkSchedule().clear_day('Monday')
    fh = open('tests/test_work_schedule.json', 'r')
    expected_data = json.load(fh)
    assert expected_data['Monday'] == {
        "12": [
            0,
            0
        ],
        "13": [
            0,
            0
        ],
        "14": [
            0,
            0
        ],
        "15": [
            0,
            0
        ],
        "16": [
            0,
            0
        ],
        "17": [
            0,
            0
        ]
    }
