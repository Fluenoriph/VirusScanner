
class LogFileParser:
    def __init__(self, target_data_validator):
        self.target_data_validator = target_data_validator
        self._matched_data = []
        self._bad_data = []

    @property
    def matched_data(self):
        return self._matched_data

    @property
    def bad_data(self):
        return self._bad_data

    def parse(self, log_file):
        with open(log_file, 'r') as file:
            data = file.readlines()

            for line in data:
                matched_object = self.target_data_validator.validate(line)

                if matched_object is not False:
                    self._matched_data.append(matched_object)
                else:
                    self._bad_data.append(line)
