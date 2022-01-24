import json


def get_path():
    with open("config.json", 'r') as fh:
        path = json.load(fh)["ws_path"]
    return path


def load_work_schedule(path):
    """Load new work schedule data as tuple"""

    file = open(path, 'r')
    file.readline()
    work_dict = {}
    for line in file:
        line = line.rstrip()
        tokens = line.split(',')
        day, star_hour, end_hour = tokens
        work_dict[day] = (int(star_hour), int(end_hour))
    return work_dict


class DataWorkSchedule:

    def __init__(self):
        """During start program open current work schedule."""

        self._ws_path = get_path()
        with open(self.ws_path(), 'r') as fp:
            data = json.load(fp)
        self._data = data

    def ws_path(self):
        return self._ws_path

    def data(self):
        return self._data

    def save_data(self, new_data):
        """Save changes in data."""

        with open(self.ws_path(), 'w') as file_handle:
            json.dump(new_data, file_handle, indent=4)

    def load_new_work_schedule(self, path):
        """Load new work schedule in specific format"""

        data = {}
        dict_days_hours = load_work_schedule(path)

        """Convert data from file to dictionaries"""

        for day in dict_days_hours:
            start_hour = dict_days_hours[day][0]
            end_hour = dict_days_hours[day][1]
            hours_dict = {}
            for i in range(start_hour, end_hour):
                hours_dict[i] = [0, 0]
            data[day] = hours_dict

        """Crate data as json file"""

        with open(self.ws_path(), 'w') as file_handle:
            json.dump(data, file_handle, indent=4)

    def clear_day(self, day):
        """Clear day values"""

        hours = self.data()[day]
        for hour in hours:
            hours[hour] = [0, 0]
        self.data()[day] = hours
        self.save_data(self.data())
