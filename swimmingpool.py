from work_schedule.work_schedule_data import DataWorkSchedule
import math
from time_functions import last_hour, days
from time_functions import first_hour
from attributes.name_tracks_data import Attributes


class Swimmingpool:
    def __init__(self):
        self._attributes = Attributes()
        tracks_sw = Attributes().tracks()
        self._name = Attributes().name()
        self._data = DataWorkSchedule()
        self._work_schedule = self.data().data()
        self._tracks_number = tracks_sw
        self._space = tracks_sw * 5
        self._max_tracks = math.floor(tracks_sw * 0.35)

    def name(self):
        return self._name

    def set_name(self, new_name):
        """Change swimming pool name"""

        self.attributes().change_name(new_name)

    def attributes(self):
        return self._attributes

    def work_schedule(self):
        return self._work_schedule

    def space(self):
        return self._space

    def data(self):
        return self._data

    def max_tracks(self):
        return self._max_tracks

    def tracks_number(self):
        return self._tracks_number

    def set_tracks_number(self, new_tracks_number):
        """Change swimming tracks number"""

        self.attributes().change_tracks(new_tracks_number)

    def check_seat(self, start_time, hours_number, current_day, number):
        """Check if there is space at the specified time."""

        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)

        for i in range(start_hour, start_hour + number_cycles):
            S_a_hour = hours_dict[str(i)]
            if S_a_hour[0] + number > self.space():
                return False

    def check_seat_and_tracks(
            self, start_time, hours_number,
            current_day, number_of_tracks):
        """Check if there is space and free tracks at the specified time."""

        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)
        number = number_of_tracks * 5

        for i in range(start_hour, start_hour + number_cycles):
            S_a_hour = hours_dict[str(i)]
            if S_a_hour[0] + number > self.space() or \
                    S_a_hour[1] + number_of_tracks > self.max_tracks():
                return False

    def check_free_term(self, start_time, hours_number, current_day, number):
        """ Check the nearest free term."""

        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)
        next_day = current_day

        """Check free term in selected day."""

        free_positions, free_hour = check_current_day_hours(
            start_hour, number_cycles, hours_dict,
            number, self.space(), self.data(), current_day)

        """Check free term in another day."""

        if free_positions != number_cycles:
            free_hour, free_positions, next_day = check_next_day(
                free_positions, free_hour, number_cycles, current_day,
                self.data(), self.work_schedule(), number, self.space())

        """Return the nearest free term information."""

        return f'Next free term {next_day} {free_hour}'

    def check_free_term_swimming_school(
            self, start_time, hours_number,
            current_day, number_of_tracks):
        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)
        number = int(number_of_tracks) * 5
        next_day = current_day

        """Check free term for swimming school in selected day."""

        free_positions, free_hour = check_current_hours_add_tracks(
            start_hour, number_cycles, hours_dict, number,
            number_of_tracks, self.space(), self.data(),
            current_day, self.max_tracks())

        """Check free term for swimming school in another day."""

        if free_positions != number_cycles:
            free_hour, free_positions, next_day = check_next_day_sw_school(
                free_positions, free_hour, number_cycles,
                current_day, self.data(), self.work_schedule(), number,
                self.space(), number_of_tracks, self.max_tracks())

        return f'Next free term {next_day} {free_hour}'

    def add_person(self, start_time, hours_number, current_day, number=1):
        """Adds people to swimming pool according to day and time."""

        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)

        for i in range(start_hour, start_hour + number_cycles):
            S_a_hour = hours_dict[str(i)]
            S_a_hour[0] += number

        """Save data."""

        self.work_schedule()[current_day] = hours_dict
        self.data().save_data(self.work_schedule())

    def add_swimming_school(
            self, start_time, hours_number,
            current_day, number_of_tracks):
        """Adds swimming_school to swimming pool according to day and time."""

        hours_dict = self.work_schedule()[current_day]
        start_hour = int(start_time)
        number_cycles = int(hours_number)
        number = number_of_tracks * 5

        for i in range(start_hour, start_hour + number_cycles):
            S_a_hour = hours_dict[str(i)]
            S_a_hour[0] += number
            S_a_hour[1] += number_of_tracks

        """Save data."""

        self.work_schedule()[current_day] = hours_dict
        self.data().save_data(self.work_schedule())


def check_current_day_hours(
        start_hour, number_cycles, hours_dict,
        number, space, data, current_day):
    """Check free term in selected day."""

    day_end_hour = int(last_hour(data, current_day))
    free_positions = 0
    free_hour = start_hour

    """Iterate current day hours to find free term."""

    for i in range(start_hour, day_end_hour + 1):
        S_a_hour = hours_dict[str(i)]
        if free_positions == number_cycles:
            break
        elif S_a_hour[0] + number > space:
            free_positions = 0
        else:
            free_positions += 1
            if free_positions == 1:
                free_hour = str(i)

    return free_positions, free_hour


def check_next_day_hours(
        free_positions, free_hour, number_cycles,
        day_start_hour, day_end_hour, hours_dict, number, space):
    """Check free hours in day."""

    """Iterate hours of the day to find free term."""

    m = 0
    while free_positions != number_cycles:
        if int(day_start_hour) + m == int(day_end_hour) + 1:
            break
        S_a_hour = hours_dict[str(int(day_start_hour) + m)]
        if S_a_hour[0] + number > space:
            free_positions = 0
        else:
            free_positions += 1
            if free_positions == 1:
                free_hour = str(int(day_start_hour) + m)
        m += 1

    return free_hour, free_positions


def check_next_day(
        free_positions, free_hour, number_cycles, current_day,
        data, work_schedule, number, space):
    """Check free term in another day."""

    """Iterate days in week to find day with free hours."""

    n = 1
    i = 0
    day_value_dict, value_day_dict = days()
    today_value = day_value_dict[current_day]
    while free_positions != number_cycles and i < 6:
        free_positions = 0
        if today_value == 6:
            today_value = -1
        if today_value + n == 7:
            n = 1
            today_value = -1
        next_day = value_day_dict[today_value + n]
        day_end_hour = last_hour(data, next_day)
        day_start_hour = first_hour(data, next_day)
        i += 1
        n += 1
        hours_dict = work_schedule[next_day]

        """Iterate hours of the day to find free term."""

        free_hour, free_positions = check_next_day_hours(
            free_positions, free_hour, number_cycles, day_start_hour,
            day_end_hour, hours_dict, number, space)

    return free_hour, free_positions, next_day


def check_current_hours_add_tracks(
        start_hour, number_cycles, hours_dict,
        number, number_of_tracks, space, data,
        current_day, max_tracks):
    """Check free term for swimming school in selected day."""

    day_end_hour = int(last_hour(data, current_day))
    free_positions = 0
    free_hour = start_hour

    """Iterate current day hours to find free term

    (free space and max tracks number not reached).
    """

    for i in range(start_hour, day_end_hour + 1):
        S_a_hour = hours_dict[str(i)]
        if free_positions == number_cycles:
            break
        elif S_a_hour[0] + number > space or\
                S_a_hour[1] + number_of_tracks > max_tracks:
            free_positions = 0
        else:
            free_positions += 1
            if free_positions == 1:
                free_hour = str(i)

    return free_positions, free_hour


def check_next_day_hours_and_tracks(
        free_positions, free_hour, number_cycles,
        day_start_hour, day_end_hour, hours_dict,
        number, space, number_of_tracks, max_tracks):
    """Check free hours and tracks in day."""

    """Iterate hours of the day to find free term."""

    m = 0
    while free_positions != number_cycles:
        if int(day_start_hour) + m == int(day_end_hour) + 1:
            break
        S_a_hour = hours_dict[str(int(day_start_hour) + m)]
        if S_a_hour[0] + number > space or\
                S_a_hour[1] + number_of_tracks > max_tracks:
            free_positions = 0
        else:
            free_positions += 1
            if free_positions == 1:
                free_hour = str(int(day_start_hour) + m)
        m += 1

    return free_hour, free_positions


def check_next_day_sw_school(
        free_positions, free_hour, number_cycles,
        current_day, data, work_schedule, number,
        space, number_of_tracks, max_tracks):
    """Check free term for swimming school in another day."""

    """Iterate days in week to find day with free hours and tracks"""

    n = 1
    i = 0
    day_value_dict, value_day_dict = days()
    today_value = day_value_dict[current_day]
    while free_positions != number_cycles and i < 6:
        free_positions = 0
        if today_value == 6:
            today_value = -1
        if today_value + n == 7:
            n = 1
            today_value = -1
        next_day = value_day_dict[today_value + n]
        day_end_hour = last_hour(data, next_day)
        day_start_hour = first_hour(data, next_day)
        i += 1
        n += 1
        hours_dict = work_schedule[next_day]

        """Iterate hours of the day to find free term for swimming school"""

        free_hour, free_positions = check_next_day_hours_and_tracks(
            free_positions, free_hour, number_cycles,
            day_start_hour, day_end_hour, hours_dict,
            number, space, number_of_tracks, max_tracks)

    return free_hour, free_positions, next_day
