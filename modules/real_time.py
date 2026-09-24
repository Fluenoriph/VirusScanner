import datetime


class CurrentTime:
    @staticmethod
    def get_current_time():
        return datetime.datetime.today().strftime('%d.%m.%Y_%H:%M:%S')
