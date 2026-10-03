"""
Application name: Virus Scanner CLI
Version: 1.0 Beta
Date: October 2026
Author: Ivan Bogdanov
Contacts: fluenoriph@gmail.com, fluenoriph@yandex.ru
"""

from typing import Annotated, Literal
from typer import Typer, Argument
import os
from rich import print
from pathlib import Path
from modules.target_data_validator.web_data_validator import WebDataValidator
from modules.program_process.web_data_process_handler import WebDataProcessHandler
from modules.program_process.file_process_handler import FileProcessHandler
from modules.app_data import TARGET_FLAG, VARIANT_FLAG, INFO_COLOR
from modules.target_data_parser.file_variant_directory_parser import FileVariantDirectoryParser
from modules.target_data_parser.log_file_parser import LogFileParser
from modules.target_data_parser.log_variant_directory_parser import LogVariantDirectoryParser
from modules.target_data_validator.file_validator import FileValidator
from modules.program_codes import CODE_10


class VirusScannerCLI:
    APP: Typer = Typer()
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
                         data: str,
                         report: Annotated[Literal['html', 'csv', 'json'], Argument()],
                         output: Annotated[Path, Argument()] = REPORT_DIRECTORY):

        print(f'\n[{INFO_COLOR}]> {CODE_10} ![/{INFO_COLOR}]')

        # --- Анализируемые данные: IP, URL, Domain --------------------------------------------------------------------
        if target is not TARGET_FLAG[3]:
            web_data_handler = WebDataProcessHandler(api_key, target, output, report)

            # --- Единичный объект -------------------------------------------------------------------------------------
            if variant is VARIANT_FLAG[0]:
                web_data_handler.process_the_object(data)

            # --- Лог файл ---------------------------------------------------------------------------------------------
            elif variant is VARIANT_FLAG[1]:
                VirusScannerCLI.process_the_log_file(WebDataValidator(target), data, web_data_handler)

            # --- Директория -------------------------------------------------------------------------------------------
            else:
                dir_parser = LogVariantDirectoryParser(data)
                dir_parser.parse()

                for log in dir_parser.parsed_data:
                    web_data_handler.output_path = VirusScannerCLI.CREATE_LOG_DIRECTORY(log)
                    VirusScannerCLI.process_the_log_file(WebDataValidator(target), log, web_data_handler)

        # --- Анализируемые данные: файлы ------------------------------------------------------------------------------
        else:
            file_data_handler = FileProcessHandler(api_key, target, output, report)

            # --- Единичный файл ---------------------
            if variant is VARIANT_FLAG[0]:
                file_data_handler.process_the_object(data)

            # --- Лог файл с полными путями к файлам -------------------------------------------------------------------
            elif variant is VARIANT_FLAG[1]:
                VirusScannerCLI.process_the_log_file(FileValidator(), data, file_data_handler)

            # --- Директория (папка) с файлами -------------------------------------------------------------------------
            else:
                dir_parser = FileVariantDirectoryParser(data)
                dir_parser.parse()

                for file in dir_parser.parsed_data:
                    file_data_handler.process_the_object(file)

    @staticmethod
    def process_the_log_file(validator, data, handler):
        log_parser = LogFileParser(validator)
        log_parser.parse(data)

        for line in log_parser.matched_data:
            handler.process_the_object(line)


VirusScannerCLI()
