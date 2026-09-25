"""
Application name: Virus Scanner CLI
Version: 1.0
Date: .... 2026 г.
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

from typing import Annotated, Literal
from typer import Typer, Argument
import os
from rich import print
from pathlib import Path
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.program_process.web_data_process_handler import WebDataProcessHandler
from modules.program_process.file_process_handler import FileProcessHandler
from modules.app_data import TARGET_FLAG, VARIANT_FLAG
from modules.target_data_parser.log_file_parser import LogFileParser
from modules.target_data_parser.log_variant_directory_parser import LogVariantDirectoryParser


class VirusScannerCLI:
    APP = Typer()
    REPORT_DIRECTORY = Path(os.path.join(os.getcwd(), 'reports'))
    CREATE_LOG_DIRECTORY = lambda log_path: os.path.join(VirusScannerCLI.REPORT_DIRECTORY,
                                                         (str(os.path.basename(str(os.path.splitext(log_path)[0])))))

    def __init__(self):
        VirusScannerCLI.APP()

    @staticmethod
    @APP.command()
    def analyse_the_data(api_key: str,
                         target: Annotated[Literal['i', 'dm', 'u', 'f'], Argument()],
                         variant: Annotated[Literal['o', 'l', 'dr'], Argument()],
                         data: str, report: Annotated[Literal['html', 'csv', 'json'], Argument()],
                         output: Annotated[str, Argument()] = str(REPORT_DIRECTORY)):

        print("[green]> Scanning started ![/green]")

        # --------------------- target is not file ---------------------
        if target is not TARGET_FLAG[3]:
            web_data_handler = WebDataProcessHandler(api_key, target, output, report)
            # --------------------- object ---------------------
            if variant is VARIANT_FLAG[0]:
                web_data_handler.process_the_object(data)
            # --------------------- log ---------------------
            elif variant is VARIANT_FLAG[1]:
                VirusScannerCLI.process_the_log_file(target, data, web_data_handler)

            # --------------------- directory ---------------------
            else:
                dir_parser = LogVariantDirectoryParser(data)
                dir_parser.parse()

                print(dir_parser.parsed_data)

                for log in dir_parser.parsed_data:
                    web_data_handler.output_path = VirusScannerCLI.CREATE_LOG_DIRECTORY(log)
                    VirusScannerCLI.process_the_log_file(target, log, web_data_handler)






        # --------------------- target is file ---------------------
        else:
            file_data_handler = FileProcessHandler(api_key)
            # --------------------- object ---------------------
            if variant is VARIANT_FLAG[0]:
                file_data_handler.process_the_object(data)
            elif variant is VARIANT_FLAG[1]:
                pass # log with file full path's
            else:
                pass # dir variant/ files in dir

    @staticmethod
    def process_the_log_file(target, data, handler):
        log_parser = LogFileParser(TargetWebDataValidator(target))
        log_parser.parse(data)

        for line in log_parser.matched_data:
            handler.process_the_object(line)


VirusScannerCLI()
