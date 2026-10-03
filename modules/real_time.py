# 'real_time.py' - функция получения настоящей даты и времени.

import datetime


def get_current_time():
    return datetime.datetime.today().strftime('%d.%m.%Y-%H:%M:%S')
