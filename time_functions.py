from datetime import datetime


def hours_range(data, current_day, input_hour):
    """Check if input is in designated range"""

    f_hour = int(first_hour(data, current_day))
    e_hour = last_hour(data, current_day)
    e_hour_fix = int(e_hour) + 1
    hour_list = [str(i) for i in range(f_hour, e_hour_fix + 1)]
    if input_hour in hour_list:
        return True
    else:
        return False


def time_interval(day, data, start_hour):
    """Give time interval number"""

    end_hour = int(last_hour(data, day)) + 1
    max_number_of_hours = end_hour - int(start_hour)
    return max_number_of_hours


def last_hour(data, current_day):
    """Give last hour in day"""

    last_hour = list(data.data()[current_day])[-1]
    return last_hour


def first_hour(data, current_day):
    """Give first hour in day"""

    first_hour = list(data.data()[current_day])[0]
    return first_hour


def current_day_schedule(data, current_day):
    """Give choosed day schedule"""

    f_hour = first_hour(data, current_day)
    e_hour = last_hour(data, current_day)
    e_hour_fix = int(e_hour) + 1
    return f'{current_day} open {f_hour} - {e_hour_fix}'


def days():
    """Return days and vales dictionaries"""

    days_list = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
    numbers = [0, 1, 2, 3, 4, 5, 6]
    day_value_dict = dict(zip(days_list, numbers))
    value_day_dict = dict(zip(numbers, days_list))
    return day_value_dict, value_day_dict


def current_time():
    """Give current time"""

    now = datetime.now().strftime('%A %H:%M')
    return now


def current_day():
    """Give current day"""

    c_day = datetime.now().strftime('%A')
    return c_day


def current_day_hour():
    """Give current hour"""

    c_day_hour = datetime.now().strftime('%H')
    return c_day_hour


def check_input_hour(fix_input):
    """Check if hour is a number"""

    try:
        if len(fix_input) <= 2:
            if type(int(fix_input)) == int:
                return True
        else:
            return False
    except Exception:
        return False


def days_dict(day_number):
    """Give expected day"""

    day_dict = {'1': 'Monday',
                '2': 'Tuesday',
                '3': 'Wednesday',
                '4': 'Thursday',
                '5': 'Friday',
                '6': 'Saturday',
                '7': 'Sunday'}
    day = day_dict[day_number]
    return day
