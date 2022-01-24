import curses
from prices.prices_data import DataPrices
from swimmingpool import Swimmingpool
from reports.daily_report import Report
from time_functions import current_day_schedule, hours_range, check_input_hour
from time_functions import days_dict, current_time, time_interval
from work_schedule.work_schedule_data import DataWorkSchedule


def my_raw_input(window, y, x, text):
    """Input for adding hours number"""

    window.addstr(5, 17, text)
    window.addstr(y, x, 'Hour format - xx or x')
    curses.echo()
    window.refresh()
    input = window.getstr(y + 1, x)
    fix_input = str(input)[2:-1]
    return fix_input


def menu_functions_input(window, y, x):
    """Input for adding vizualized text"""

    curses.echo()
    window.refresh()
    input = window.getstr(y + 1, x)
    fix_input = str(input)[2:-1]
    return fix_input


def new_window(begin_y, begin_x, height, width):
    """Initialize new window"""

    win = curses.newwin(height, width, begin_y, begin_x)
    return win


def add_first_screen(window):
    """Main screen"""

    window.addstr(1, 1, "Choose number")
    window.addstr(2, 1, "1. Menu")
    window.addstr(3, 1, "2. Add People")
    window.addstr(4, 1, "3. Add Swimming School")
    window.addstr(5, 1, "4. Space and tracks preview")


def add_menu_screen(window):
    """Menu screen"""

    window.clear()
    window.addstr(1, 1, "Choose number")
    window.addstr(2, 1, "1. Change swimmingpool name")
    window.addstr(3, 1, "2. Change swimmingpool number of tracks")
    window.addstr(4, 1, "3. Change work_schedule file")
    window.addstr(5, 1, "4. Change price-list file")
    numbers = [str(item) for item in list(range(1, 5))]
    input = window.getkey()
    while input != 'q':
        if input in numbers:
            window.clear()
            return input
        input = window.getkey()
    window.clear()
    return False


def name_screen(win, pool):
    """Change name screen"""

    win.clear()
    win.addstr(7, 12, "Input new name")
    choice = menu_functions_input(win, 7, 12)
    if choice == 'q':
        win.clear()
        return False
    else:
        win.clear()
        win.addstr(7, 17, "Name changed")
        pool.set_name(choice)
        win.refresh()
        win.getch()
        return False


def tracks_screen(win, pool):
    """Change tracks screen"""

    choice = ''
    while choice != 'q':
        win.clear()
        win.addstr(7, 12, "Input new number of tracks")
        choice = menu_functions_input(win, 7, 12)
        try:
            tracks_num = int(choice)
            win.clear()
            win.addstr(7, 17, "Tracks has been changed")
            pool.set_tracks_number(tracks_num)
            win.refresh()
            win.getch()
            return
        except Exception:
            if choice != 'q':
                win.clear()
                win.addstr(7, 6, "Number of tracks must be integer number")
                win.refresh()
                win.getch()
    win.clear()
    return False


def number_hours_screen(win, day, data, start_hour):
    """Screen for adding hours number"""

    choice = ''
    while choice != 'q':
        win.clear()
        win.addstr(7, 12, "Input number of hours")
        choice = menu_functions_input(win, 7, 12)
        max_number = time_interval(day, data, start_hour)
        try:
            input_hours_num = int(choice)
            if input_hours_num > max_number or input_hours_num == 0:
                win.clear()
                win.addstr(7, 6, f"Hours out of range Max: {max_number}")
                win.refresh()
                win.getch()
                continue
            win.clear()
            win.refresh()
            return input_hours_num
        except Exception:
            if choice != 'q':
                win.clear()
                win.addstr(7, 6, "Number of hours must be integer number")
                win.refresh()
                win.getch()
    win.clear()
    return False


def work_schedule_file_screen(win, data):
    """Screen for changing work schedule file"""

    win.clear()
    win.addstr(7, 12, "Input work_schedule file path")
    choice = menu_functions_input(win, 7, 12)
    while choice != 'q':
        try:
            data.load_new_work_schedule(choice)
            win.clear()
            win.addstr(7, 17, "Work schedule changed")
            win.refresh()
            win.getch()
            return
        except Exception:
            win.clear()
            win.addstr(7, 5, "File does not exist or wrong file format")
            win.refresh()
            win.getch()
        win.clear()
        win.addstr(7, 12, "Input work_schedule file path")
        choice = menu_functions_input(win, 7, 12)
    return False


def free_terms_data_screen(day, data, pool, win):
    """Free space and tracks screen"""

    current_day_hours = data.data()[day]
    text = f'   {day}, Free Space, Free Tracks\n'
    for hour in current_day_hours:
        free_space = pool.space() - current_day_hours[hour][0]
        free_tracks = pool.max_tracks() - current_day_hours[hour][1]
        line = f'      {hour}:       {free_space},           {free_tracks}\n'
        text += line
    win.clear()
    win.addstr(1, 1, text)
    win.refresh()
    win.getch()


def prices_file_screen(win, prices):
    """Screen for changing prices file"""

    win.clear()
    win.addstr(7, 12, "Input prices file path")
    choice = menu_functions_input(win, 7, 12)
    while choice != 'q':
        try:
            prices.load_new_prices(choice)
            win.clear()
            win.addstr(7, 17, "Prices changed")
            win.refresh()
            win.getch()
            return
        except Exception:
            win.clear()
            win.addstr(7, 5, "File does not exist or wrong file format")
            win.refresh()
            win.getch()
        win.clear()
        win.addstr(7, 12, "Input prices file path")
        choice = menu_functions_input(win, 7, 12)
    win.clear()
    return False


def days_of_the_week(window):
    """Chose day screen"""

    window.clear()
    window.addstr(1, 1, "Choose day")
    window.addstr(2, 1, "1. Monday")
    window.addstr(3, 1, "2. Tuesday")
    window.addstr(4, 1, "3. Wednesday")
    window.addstr(5, 1, "4. Thursday")
    window.addstr(6, 1, "5. Friday")
    window.addstr(7, 1, "6. Saturday")
    window.addstr(8, 1, "7. Sunday")
    numbers = [str(item) for item in list(range(1, 8))]
    input = window.getkey()
    while input != 'q':
        if input in numbers:
            window.clear()
            return input
        else:
            input = window.getkey()
    window.clear()
    return False


def people_screen(window, prices_data, day):
    """Screen for choosing customer"""

    window.clear()
    clients = {
        '1': 'Adult',
        '2': 'Kid',
        '3': 'Kid_under_5_years_old',
        '4': 'Disabled',
        '5': 'Pensioner',
        '6': 'Student'
    }
    window.addstr(1, 1, "Choose option : Price")
    window.addstr(
        2, 1, f"1. Adult : {prices_data.get_price('Adult', day)}")
    window.addstr(
        3, 1, f"2. Kid : {prices_data.get_price('Kid', day)}")
    window.addstr(
        4, 1,
        f"3. {clients['3']} : {prices_data.get_price(clients['3'], day)}")
    window.addstr(
        5, 1, f"4. Disabled : {prices_data.get_price('Disabled', day)}")
    window.addstr(
        6, 1, f"5. Pensioner : {prices_data.get_price('Pensioner', day)}")
    window.addstr(
        7, 1, f"6. Student : {prices_data.get_price('Student', day)}")

    numbers = [str(item) for item in list(range(1, 8))]
    input = window.getkey()
    while input != 'q':
        if input in numbers:
            client = clients[input]
            window.clear()
            return client
        else:
            input = window.getkey()
    window.clear()
    return False


def cost_screen(win, price, num, day, input, prices, integer):
    """Screen for showing current ticket cost"""

    win.clear()
    curses.noecho()
    promo_hour = prices.get_till_hour_promo(day)
    actuall_hour = int(input)
    if actuall_hour < promo_hour:
        ticket_cost = round(price * num * integer * 0.8, 1)
    else:
        ticket_cost = price * num * integer
    win.addstr(5, 10, 'Please y to accept or n to discard')
    win.addstr(7, 17, f'It will cost {ticket_cost}')
    key = win.getkey()
    while key != 'q':
        if key == 'y':
            win.clear()
            win.refresh()
            return True, ticket_cost
        elif key == 'n':
            win.clear()
            win.refresh()
            return False, ticket_cost
        key = win.getkey()
    win.clear()
    return False, ticket_cost


def number_of_people(window, pool):
    """Screen for adding number of people"""

    max_num = pool.space() + 1
    numbers = [str(item) for item in list(range(1, max_num))]
    number_of_people = ''
    while number_of_people != 'q':
        window.clear()
        window.refresh()
        window.addstr(7, 8, f"Input number of people Max: {max_num - 1}")
        number_of_people = menu_functions_input(window, 7, 12)
        try:
            int(number_of_people)
        except Exception:
            if number_of_people != 'q':
                window.clear()
                window.addstr(7, 14, "Wrong number of people")
                window.refresh()
                window.getch()
            continue
        if number_of_people in numbers:
            window.clear()
            return int(number_of_people)
        else:
            window.clear()
            window.addstr(7, 10, f'Number must be less than {max_num}')
            window.refresh()
            window.getch()
    window.clear()
    return False


def number_of_tracks(window, pool):
    """Screen for adding number of tracks"""

    max_track_number = pool.max_tracks()
    numbers = [str(item) for item in list(range(1, int(max_track_number) + 1))]
    window.addstr(
        7, 6, f"Input number of tracks Max number: {max_track_number}")
    tracks_num = ''
    while tracks_num != 'q':
        window.addstr(
            7, 6, f"Input number of tracks Max number: {max_track_number}")
        tracks_num = window.getkey()
        try:
            if int(tracks_num) > max_track_number:
                window.clear()
                window.addstr(
                    7, 10, f"Tracks number cannot be > {max_track_number}")
                window.refresh()
                window.getch()
                continue
            elif tracks_num in numbers:
                window.clear()
                return int(tracks_num)
        except Exception:
            window.clear()
            if tracks_num != 'q':
                window.addstr(
                    7, 10, f"Tracks number cannot be > {max_track_number}")
                window.refresh()
                window.getch()
                window.clear()
    window.clear()
    return False


def hour_input_interface(win, text, data, day):
    """Screen for start hour input"""

    choice = ''
    while choice != 'q':
        win.clear()
        choice = my_raw_input(win, 7, 12, text)
        result = check_input_hour(choice)
        if result is True:
            if hours_range(data, day, choice) is True:
                return choice
            else:
                win.clear()
                win.addstr(7, 17, "Hour out of range")
                win.refresh()
                win.getch()
                continue
        elif result is False and choice != 'q':
            win.clear()
            win.addstr(7, 17, "Wrong hour format")
            win.getch()
    win.clear()
    return False


def add_people_screen(win, second_win, price_data, pool):
    """First screen for adding clients to swimmingpool
    It gains input from user
    """

    num = days_of_the_week(win)
    if false_argument(win, second_win, num) is False:
        return False

    day = days_dict(num)
    second_win.addstr(7, 2, current_day_schedule(pool.data(), day))
    second_win.refresh()
    client = people_screen(win, price_data, day)
    if false_argument(win, second_win, client) is False:
        return False

    price = price_data.get_price(client, day)
    num_p = number_of_people(win, pool)
    if false_argument(win, second_win, num_p) is False:
        return False

    input_stime = hour_input_interface(
        win, "Input start hour", pool.data(), day)
    if false_argument(win, second_win, input_stime) is False:
        return False

    input_hours_num = number_hours_screen(win, day, pool.data(), input_stime)
    if false_argument(win, second_win, input_hours_num) is False:
        return False
    second_win.clear()
    second_win.refresh()
    funct_list = [input_stime, input_hours_num, num_p, price, client, day]

    return funct_list


def false_argument(win, second_win, argument):
    """Check return arguments for functions"""

    if argument is False:
        win.clear()
        second_win.clear()
        return False
    return True


def add_sw_school_screen(win, second_win, price_data, pool):
    """First screen for adding swimming schools to swimmingpool
    It gains input from user
    """

    num = days_of_the_week(win)
    if false_argument(win, second_win, num) is False:
        return False

    day = days_dict(num)
    second_win.addstr(7, 2, current_day_schedule(pool.data(), day))
    second_win.refresh()
    client = 'swimming_school'
    price = price_data.get_price(client, day)

    tracks_num = number_of_tracks(win, pool)
    if false_argument(win, second_win, tracks_num) is False:
        return False

    input_stime = hour_input_interface(
        win, "Input start hour", pool.data(), day)
    if false_argument(win, second_win, input_stime) is False:
        return False

    input_hours_num = number_hours_screen(win, day, pool.data(), input_stime)
    if false_argument(win, second_win, input_hours_num) is False:
        return False
    second_win.clear()
    second_win.refresh()
    funct_list = [input_stime, input_hours_num, tracks_num, price, client, day]

    return funct_list


def add_people_screen_2p(
        win, input_stime, input_hours_num, day, num_p, price,
        prices, integer, pool, output, report, client):
    """Second screen for adding clients to swimmingpool
    It gives information about space and adds client to data"""

    if output is False:
        win.clear()
        win.addstr(7, 17, 'There is no space')
        term = pool.check_free_term(input_stime, input_hours_num, day, num_p)
        win.addstr(9, 10, term)
        win.refresh()
        win.getch()
    else:
        ticket = cost_screen(
            win, price, num_p, day,
            input_stime, prices, integer)
        if ticket[0] is True:
            input_etime = int(input_stime) + int(input_hours_num)
            report.write_line(
                client, num_p, ticket[1], day, input_stime, input_etime)
            pool.add_person(input_stime, input_hours_num, day, num_p)
            win.addstr(
                7, 10, f'{input_stime} - {input_etime} {day} added {num_p} ')
            win.refresh()
            win.getch()


def add_sw_school_screen_2p(
        win, input_stime, input_hours_num, day, tracks_num, price,
        prices, integer, pool, output, report, client):
    """Second screen for adding swimming schools to swimmingpool.
    It gives information about space, tracks and adds client to data"""

    if output is False:
        win.clear()
        win.addstr(7, 17, 'There is no space')
        term = pool.check_free_term_swimming_school(
            input_stime, input_hours_num, day, tracks_num)
        win.addstr(9, 10, term)
        win.refresh()
        win.getch()
    else:
        ticket = cost_screen(
            win, price, tracks_num, day,
            input_stime, prices, integer)
        if ticket[0] is True:
            input_etime = int(input_stime) + int(input_hours_num)
            report.write_line(
                client, tracks_num, ticket[1], day, input_stime, input_etime)
            pool.add_swimming_school(
                input_stime, input_hours_num, day, tracks_num)
            win.addstr(
                7, 10,
                f'{input_stime} - {input_etime} {day} added {tracks_num} ')
            win.refresh()
            win.getch()


def start_screen():
    """Main function. Bring up all screens"""

    """Initialize screens"""

    stdscr = curses.initscr()
    win = new_window(3, 30, 20, 50)
    second_win = new_window(3, 80, 20, 25)
    time_win = new_window(1, 80, 2, 25)
    curses.start_color()
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
    win.bkgd(curses.color_pair(2))
    time_win.bkgd(curses.color_pair(3))
    second_win.bkgd(curses.color_pair(4))
    input = ''
    while input != 'q':

        """Load main data and first screen attributes"""

        data = DataWorkSchedule()
        pool = Swimmingpool()
        prices = DataPrices()
        report = Report()
        stdscr.addstr(2, 47, "                               ")
        stdscr.addstr(1, 45, "WELCOME TO SWIMMINGPOOL")
        stdscr.addstr(2, 47, f'"{pool.name()}" tracks: {pool.tracks_number()}')
        time_win.addstr(0, 2, current_time())
        stdscr.refresh()
        time_win.refresh()
        second_win.addstr(18, 2, "Press q to Exit")
        second_win.refresh()
        win.clear()
        add_first_screen(win)
        win.refresh()
        curses.noecho()

        """Get input and choose another screen"""

        input = win.getkey()
        if input == '1':

            """Input for choosing options"""

            inp = add_menu_screen(win)
            if inp is False:
                continue
            elif inp == '1':
                new_name = name_screen(win, pool)
                if new_name is False:
                    continue
            elif inp == '2':
                new_tracks = tracks_screen(win, pool)
                if new_tracks is False:
                    continue
            elif inp == '3':
                new_ws_file = work_schedule_file_screen(win, data)
                if new_ws_file is False:
                    continue
            elif inp == '4':
                new_prices = prices_file_screen(win, prices)
                if new_prices is False:
                    continue

            """Initialize add people screen"""

        elif input == '2':
            fl = add_people_screen(win, second_win, prices, pool)
            if fl is False:
                continue
            else:
                integer = fl[1]
            output = pool.check_seat(fl[0], fl[1], fl[5], fl[2])
            second_win.clear()
            win.refresh()
            add_people_screen_2p(
                win, fl[0], fl[1], fl[5], fl[2], fl[3],
                prices, integer, pool, output, report, fl[4])

            """Initialize add swimming school screen"""

        elif input == '3':
            flsw = add_sw_school_screen(win, second_win, prices, pool)
            if flsw is False:
                continue
            else:
                integer = flsw[1]
            output = pool.check_seat_and_tracks(
                flsw[0], flsw[1], flsw[5], flsw[2])
            second_win.clear()
            win.refresh()
            add_sw_school_screen_2p(
                win, flsw[0], flsw[1], flsw[5], flsw[2],
                flsw[3], prices, integer, pool, output, report, flsw[4])

        elif input == '4':
            win.clear()
            num = days_of_the_week(win)
            day = days_dict(num)
            free_terms_data_screen(day, data, pool, win)

    """End session"""

    curses.endwin()


if __name__ == "__main__":
    start_screen()
