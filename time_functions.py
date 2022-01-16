from datetime import datetime


"""Check if input is in designated range"""


def hours_range(data, current_day, input_hour):
    f_hour = int(first_hour(data, current_day))
    e_hour = last_hour(data, current_day)
    e_hour_fix = int(e_hour) + 1
    hour_list = [str(i) for i in range(f_hour, e_hour_fix + 1)]
    if input_hour in hour_list:
        return True
    else:
        return False


"""Give time interval number"""


def time_interval(day, data, start_hour):
    end_hour = int(last_hour(data, day)) + 1
    max_number_of_hours = end_hour - int(start_hour)
    return max_number_of_hours


"""Give last hour in day"""


def last_hour(data, current_day):
    last_hour = list(data.data()[current_day])[-1]
    return last_hour


"""Give first hour in day"""


def first_hour(data, current_day):
    first_hour = list(data.data()[current_day])[0]
    return first_hour


"""Give choosed day schedule"""


def current_day_schedule(data, current_day):
    f_hour = first_hour(data, current_day)
    e_hour = last_hour(data, current_day)
    e_hour_fix = int(e_hour) + 1
    return f'{current_day} open {f_hour} - {e_hour_fix}'


"""Return days and vales dictionaries"""


def days():
    days_list = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
    numbers = [0, 1, 2, 3, 4, 5, 6]
    day_value_dict = dict(zip(days_list, numbers))
    value_day_dict = dict(zip(numbers, days_list))
    return day_value_dict, value_day_dict


"""Give current time"""


def current_time():
    now = datetime.now().strftime('%A %H:%M')
    return now


"""Give current day"""


def current_day():
    c_day = datetime.now().strftime('%A')
    return c_day


"""Give current hour"""


def current_day_hour():
    c_day_hour = datetime.now().strftime('%H')
    return c_day_hour


"""Check if hour is a number"""


def check_input_hour(fix_input):
    try:
        if len(fix_input) <= 2:
            if type(int(fix_input)) == int:
                return True
        else:
            return False
    except Exception:
        return False


"""Give expected day"""


def days_dict(day_number):
    day_dict = {'1': 'Monday',
                '2': 'Tuesday',
                '3': 'Wednesday',
                '4': 'Thursday',
                '5': 'Friday',
                '6': 'Saturday',
                '7': 'Sunday'}
    day = day_dict[day_number]
    return day
