# 'log_file_parser.py' - парсер лог файла с валидацией строк данных по целевому типу (ip, domain, url, file).

class LogFileParser:
    def __init__(self, data_validator):
        self.data_validator = data_validator
        self._matched_data = []

    @property
    def matched_data(self):
        return self._matched_data

    def parse(self, log_file):
        with open(log_file, 'r') as file:
            data = file.readlines()

            for line in data:
                clear_line = line.rstrip('\n')

                match = self.data_validator.validate(clear_line)

                if match:
                    self.matched_data.append(clear_line)
