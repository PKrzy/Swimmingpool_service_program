from work_schedule.work_schedule_data import DataWorkSchedule
from time_functions import current_day
from reports.daily_report import Report


"""Generate todays report"""


def generate_report():
    day = current_day()
    Report().write_today_report()
    DataWorkSchedule().clear_day(day)


if __name__ == "__main__":
    generate_report()
