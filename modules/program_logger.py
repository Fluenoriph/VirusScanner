# Файл 'program_loger.py': класс для записи действий программы в текстовый файл.

import logging


logging.basicConfig(
    filename='program_log.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)
