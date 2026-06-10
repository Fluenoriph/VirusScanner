"""
Program name: Virus Scanner
Version: 1.0
Date:  2026 г.
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

import platform
import os
import sys
from typing import Annotated
import typer
#from modules.argument_parser import ArgumentParser
#from modules.program_process import ProgramProcess
from modules.base_report_generator import BaseReportGenerator


class VirusScannerCLI:
    APP = typer.Typer()
    PROGRAM_DIRECTORY = os.getcwd() # ???

    def __init__(self):
        VirusScannerCLI.APP()

    @staticmethod
    @APP.command()
    def analyse_the_data(virus_total_api_key: str, data_to_analyse: str,
                         ip: Annotated[bool, typer.Argument()] = False,
                         domain: Annotated[bool, typer.Argument()] = False,
                         url: Annotated[bool, typer.Argument()] = False,
                         file: Annotated[bool, typer.Argument()] = False,
                         obj: Annotated[bool, typer.Argument()] = False,
                         log: Annotated[bool, typer.Argument()] = False,
                         directory: Annotated[bool, typer.Argument()] = False,
                         output_path: Annotated[str, typer.Argument()] = PROGRAM_DIRECTORY,
                         report_format: Annotated[str, typer.Argument()] = BaseReportGenerator.REPORT_FILE_TYPE[2]):

        def variant(data):
            if obj:
                return data

        for data_type in (ip, domain, url, file):


        if ip:





        pass


















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
