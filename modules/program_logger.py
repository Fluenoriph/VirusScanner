# Файл 'program_loger.py': класс для записи действий программы в текстовый файл.

import logging


class ProgramLogger:
    def __init__(self):
        self._logger = logging.getLogger()
        #self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler(r'./program_log.log')  # windows ?
        handler.setFormatter(formatter)

        self._logger.addHandler(handler)

    @property
    def logger(self):
        return self._logger

logger = ProgramLogger()
