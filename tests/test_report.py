from reports.daily_report import Report


def test_report_file():
    assert Report().report_file() == 'reports/report.txt'


def test_file_content(monkeypatch):
    def fake_path(k):
        return 'tests/test_report.txt'
    monkeypatch.setattr(Report, 'report_file', fake_path)
    content = Report().file_content()
    assert content.read() == 'Day, Time, Client, Number, Price\n'


def test_clear_file(monkeypatch):
    def fake_path(k):
        return 'tests/test_report.txt'
    monkeypatch.setattr(Report, 'report_file', fake_path)
    Report().clear_file()
    content = (Report().file_content()).read()
    assert content == 'Day, Time, Client, Number, Price\n'


def test_file_write_line(monkeypatch):
    def fake_path(k):
        return 'tests/test_report.txt'
    monkeypatch.setattr(Report, 'report_file', fake_path)
    Report().write_line('Kid', 10, 200, 'Monday', 10, 12)
    content = Report().file_content()
    assert content.read() == """Day, Time, Client, Number, Price
Monday, 10-12, Kid, 10, 200\n"""
    Report().clear_file()
