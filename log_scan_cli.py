"""
Название утилиты: Log Scanner
Версия: 0.9
Дата: Февраль 2026 г.
Автор: Богданов Иван
Контакты: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import platform
import os.path
import sys
import glob
from modules.argument_parser import ArgumentParser
from modules.program_process import ProgramProcess

# Возможно это будет классом.
argument_parser = ArgumentParser()

if os.path.isfile(argument_parser.arguments.logfile):
    app = ProgramProcess(argument_parser.arguments.logfile,
                         argument_parser.arguments.apikey,
                         argument_parser.arguments.output,
                         argument_parser.arguments.format)

elif os.path.isdir(argument_parser.arguments.logfile):
    match platform.system():
        case "Linux":
            SLASH = '/'
        case "Windows":
            SLASH = '\\'
        case _:
            sys.exit()

    files = (glob.glob(rf'{argument_parser.arguments.logfile}{SLASH}*.log') +
             glob.glob(rf'{argument_parser.arguments.logfile}{SLASH}*.txt'))

    for file in files:
        app = ProgramProcess(file, argument_parser.arguments.apikey,
                             argument_parser.arguments.output, argument_parser.arguments.format)
