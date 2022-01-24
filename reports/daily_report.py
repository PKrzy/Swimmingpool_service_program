import os
from datetime import datetime
import json


def get_path_report():
    with open("config.json", 'r') as fh:
        path = json.load(fh)["report_path"]
    return path


class Report:

    def __init__(self):
        """During start program open current report file."""

        self._report_file = get_path_report()
        if os.path.getsize(self.report_file()) == 0:
            file_wrie = open(self.report_file(), 'w')
            file_wrie.writelines('Day, Time, Client, Number, Price\n')

    def report_file(self):
        return self._report_file

    def file_content(self):
        """Read current report file data"""

        file_content = open(self.report_file(), 'r')
        return file_content

    def write_line(self, client, num, price, day, stime, etime):
        """Write line about receipt in file"""

        file = open(self.report_file(), 'a')
        file.write(f'{day}, {stime}-{etime}, {client}, {num}, {price}\n')

    def clear_file(self):
        """Clear file"""

        open(self.report_file(), 'w').close()

    def write_today_report(self):
        """Write todat report. Make new file and clear current data"""

        todays_date = datetime.now().strftime('%d_%m_%Y')
        report_name = f'Report_{todays_date}'
        report_file = open(f'reports/{report_name}.txt', 'w')
        report_file.writelines(self.file_content())
        self.clear_file()
