# Файл 'program_loger.py': класс для записи действий программы в текстовый файл.

import logging


class ProgramLogger:
    def __init__(self):
        self._logger = logging.getLogger('ProgramLogger')
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(r'./program_log.log')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    @property
    def logger(self):
        return self._logger
