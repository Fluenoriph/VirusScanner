import abc
import os


class BaseProgramProcess(abc.ABC):
    def __init__(self, cli_arguments):
        self.api_key = cli_arguments[0]
        self.report_format = cli_arguments[3]
        self._result_data = []

        if not os.path.exists(cli_arguments[2]):
            os.makedirs(cli_arguments[2])  # raise ??
            self.output_path = cli_arguments[2]

    @property
    def result_data(self):
        return self._result_data
