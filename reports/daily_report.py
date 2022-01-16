import os
from datetime import datetime


class Report:

    """During start program open current report file."""

    def __init__(self):
        self._report_file = 'reports/report.txt'
        if os.path.getsize(self.report_file()) == 0:
            file_wrie = open(self.report_file(), 'w')
            file_wrie.writelines('Day, Time, Client, Number, Price\n')

    def report_file(self):
        return self._report_file

    """Read current report file data"""

    def file_content(self):
        file_content = open(self.report_file(), 'r')
        return file_content

    """Write line about receipt in file"""

    def write_line(self, client, num, price, day, stime, etime):
        file = open(self.report_file(), 'a')
        file.write(f'{day}, {stime}-{etime}, {client}, {num}, {price}\n')

    """Clear file"""

    def clear_file(self):
        open(self.report_file(), 'w').close()

    """Write todat report. Make new file and clear current data"""

    def write_today_report(self):
        todays_date = datetime.now().strftime('%d_%m_%Y')
        report_name = f'Report_{todays_date}'
        report_file = open(f'reports/{report_name}.txt', 'w')
        report_file.writelines(self.file_content())
        self.clear_file()
